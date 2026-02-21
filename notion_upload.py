import os
import re
import requests
import json
import sys
import time

# Ensure print statements flush
def print_flush(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

# Notion API configuration
NOTION_TOKEN = "REDACTED_NOTION_TOKEN"
PARENT_PAGE_ID = "30beab20-0eed-80a0-80a1-cf6a2ad73acd"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def convert_markdown_to_blocks(markdown_text):
    blocks = []
    lines = markdown_text.split('\n')
    
    # Parsing states
    in_code_block = False
    in_table = False
    current_code_block = []
    current_table_headers = []
    current_table_rows = []
    
    for line in lines:
        line = line.rstrip()
        
        # Code block handling
        if line.startswith('```'):
            if in_code_block:
                # End of code block
                blocks.append({
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": '\n'.join(current_code_block)}}],
                        "language": line[3:] if len(line) > 3 else "plain text"
                    }
                })
                current_code_block = []
                in_code_block = False
            else:
                # Start of code block
                in_code_block = True
                current_code_block = []
            continue
        
        if in_code_block:
            current_code_block.append(line)
            continue
        
        # Table handling
        if line.startswith('|'):
            if not in_table:
                # First table line (headers)
                in_table = True
                current_table_headers = [h.strip() for h in line.strip('|').split('|')]
                continue
            elif line.startswith('| ---'):
                # Table separator line, skip
                continue
            else:
                # Table row
                row_cells = [cell.strip() for cell in line.strip('|').split('|')]
                current_table_rows.append(row_cells)
                continue
        
        # If we were in a table, now convert it
        if in_table:
            # Create table block
            table_block = {
                "type": "table",
                "table": {
                    "table_width": len(current_table_headers),
                    "has_column_header": True,
                    "has_row_header": False,
                    "children": []
                }
            }
            
            # Add headers and rows as children
            all_rows = [current_table_headers] + current_table_rows
            for row_data in all_rows:
                table_row = {
                    "type": "table_row",
                    "table_row": {
                        "cells": [[{"type": "text", "text": {"content": cell}}] for cell in row_data]
                    }
                }
                table_block["table"]["children"].append(table_row)
            
            blocks.append(table_block)
            
            # Reset table states
            in_table = False
            current_table_headers = []
            current_table_rows = []
        
        # Heading handling
        if line.startswith('# '):
            blocks.append({
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                }
            })
        elif line.startswith('## '):
            blocks.append({
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": line[3:]}}]
                }
            })
        elif line.startswith('### '):
            blocks.append({
                "type": "heading_3",
                "heading_3": {
                    "rich_text": [{"type": "text", "text": {"content": line[4:]}}]
                }
            })
        
        # Divider handling
        elif line.strip() == '---':
            blocks.append({"type": "divider", "divider": {}})
        
        # Bullet list handling
        elif line.startswith('- '):
            blocks.append({
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": line[2:]}}]
                }
            })
        
        # Paragraph handling (non-empty lines that don't match other types)
        elif line.strip() and not line.startswith(('# ', '## ', '### ', '- ', '|')):
            # Handle bold text
            bold_pattern = re.compile(r'\*\*(.*?)\*\*')
            rich_text = []
            
            # Split the line into bold and non-bold parts
            parts = bold_pattern.split(line)
            for part in parts:
                if bold_pattern.match(f"**{part}**"):
                    rich_text.append({
                        "type": "text",
                        "text": {"content": part},
                        "annotations": {"bold": True}
                    })
                elif part:
                    rich_text.append({
                        "type": "text",
                        "text": {"content": part}
                    })
            
            blocks.append({
                "type": "paragraph",
                "paragraph": {
                    "rich_text": rich_text
                }
            })
    
    return blocks

def create_notion_page(title, blocks, parent_page_id):
    url = "https://api.notion.com/v1/pages"
    
    # Ensure we don't exceed the first 100 blocks
    first_batch = blocks[:100]
    
    payload = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "title": [
                    {
                        "type": "text",
                        "text": {"content": title}
                    }
                ]
            }
        },
        "children": first_batch
    }
    
    try:
        print_flush(f"Creating page: {title}")
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        
        if response.status_code == 200:
            page_url = response.json()["url"]
            print_flush(f"Page created successfully: {page_url}")
            return page_url
        else:
            print_flush(f"Error creating page: {response.text}")
            return None
    except Exception as e:
        print_flush(f"Exception in create_notion_page: {e}")
        return None

def append_blocks_to_page(page_url, blocks):
    # Extract page ID from the URL
    match = re.search(r'-([a-f0-9]+)$', page_url)
    if not match:
        print_flush(f"Could not extract page ID from URL: {page_url}")
        return
    
    page_id = match.group(1)
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    payload = {
        "children": blocks
    }
    
    try:
        print_flush(f"Appending {len(blocks)} blocks to page")
        response = requests.patch(url, headers=HEADERS, data=json.dumps(payload))
        
        if response.status_code != 200:
            print_flush(f"Error appending blocks: {response.text}")
        else:
            print_flush("Successfully appended blocks to page.")
    except Exception as e:
        print_flush(f"Exception in append_blocks_to_page: {e}")

def process_file(file_path, title, parent_page_id):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        print_flush(f"Processing file: {file_path}")
        blocks = convert_markdown_to_blocks(markdown_text)
        
        # Split blocks into batches of 100
        page_url = None
        for i in range(0, len(blocks), 100):
            batch_blocks = blocks[i:i+100]
            if i == 0:
                # First batch creates the page
                page_url = create_notion_page(title, batch_blocks, parent_page_id)
                if not page_url:
                    print_flush(f"Failed to create page for {title}")
                    break
            else:
                # Subsequent batches append to the page
                if page_url:
                    # Add a small delay between batch uploads to avoid rate limiting
                    time.sleep(1)
                    append_blocks_to_page(page_url, batch_blocks)
        
        return page_url
    except Exception as e:
        print_flush(f"Exception in process_file: {e}")
        return None

# Files to process
files = [
    ("/Users/janet/.openclaw/workspace/analemma/shopify-audit.md", "Shopify Beauty Brand Audit -- Competitive Analysis"),
    ("/Users/janet/.openclaw/workspace/analemma/pre-launch-content-calendar-old.md", "Sweet Treat Pre-Launch Content Calendar (Original Mar 8)"),
    ("/Users/janet/.openclaw/workspace/analemma/influencer-research.md", "Singapore Micro-Influencer Research -- Sweet Treat Launch")
]

# Process each file
created_pages = []
for file_path, title in files:
    print_flush(f"\nProcessing {file_path}")
    page_url = process_file(file_path, title, PARENT_PAGE_ID)
    if page_url:
        print_flush(f"Final page URL: {page_url}")
        created_pages.append((title, page_url))
    else:
        print_flush(f"Failed to process {file_path}")

# Print summary
print_flush("\n=== NOTION UPLOAD SUMMARY ===")
for title, url in created_pages:
    print_flush(f"{title}: {url}")
print_flush("\n=== UPLOAD COMPLETE ===")

# Final flush to ensure all output is printed
sys.stdout.flush()