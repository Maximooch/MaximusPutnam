#!/usr/bin/env python3
"""
Build script for MaximusPutnam.com
Reads YAML content files and injects into index.html
"""

import yaml
from pathlib import Path
import re

CONTENT_DIR = Path("content")
TEMPLATE_FILE = Path("index.html")
OUTPUT_FILE = Path("index.html")


def parse_markdown(text):
    """Convert **bold** to <strong>bold</strong>"""
    if not isinstance(text, str):
        text = str(text)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)


def build_window_content(window_id, data):
    """Build HTML content for a window section"""
    html_parts = []

    # Title
    if 'title' in data:
        html_parts.append(f"<h2>{data['title']}</h2>")

    # Body paragraphs
    if 'body' in data:
        for item in data['body']:
            if 'paragraph' in item:
                html_parts.append(f"<p>{parse_markdown(item['paragraph'])}</p>")

    # Intro (raw HTML, for writing section)
    if 'intro' in data:
        html_parts.append(data['intro'])

    # List
    if 'list' in data:
        html_parts.append('<ul>')
        for item in data['list']:
            if isinstance(item, dict):
                item_text = list(item.values())[0] if item else ''
            else:
                item_text = item
            html_parts.append(f"        <li>{parse_markdown(item_text)}</li>")
        html_parts.append('      </ul>')

    # Pills
    if 'pills' in data:
        html_parts.append('<div>')
        for pill in data['pills']:
            html_parts.append(f'        <span class="pill">{pill}</span>')
        html_parts.append('      </div>')

    # Footnote
    if 'footnote' in data:
        html_parts.append(f'<p class="footnote">{parse_markdown(data["footnote"])}</p>')

    return '\n      '.join(html_parts)


def update_window_title(html, window_id, title):
    """Update the window title in titlebar"""
    pattern = rf'(<section class="window" id="{window_id}"[^>]*>.*?<div class="title">)(.*?)(</div>)'
    replacement = rf'\1{title}\3'
    return re.sub(pattern, replacement, html, flags=re.DOTALL)


def update_window_content(html, window_id, content):
    """Update the content div inside a window"""
    pattern = rf'(<section class="window" id="{window_id}"[^>]*>.*?<div class="content">)(.*?)(</div>\s*</section>)'

    def replace_content(match):
        return match.group(1) + '\n      ' + content + '\n    ' + match.group(3)

    return re.sub(pattern, replace_content, html, flags=re.DOTALL)


def main():
    # Read template
    html = TEMPLATE_FILE.read_text()

    # Process each content file
    for yaml_file in CONTENT_DIR.glob("*.yaml"):
        window_id = yaml_file.stem
        print(f"Processing {window_id}...")

        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        # Update window title
        if 'window_title' in data:
            html = update_window_title(html, window_id, data['window_title'])

        # Update window content
        content = build_window_content(window_id, data)
        html = update_window_content(html, window_id, content)

    # Write output
    OUTPUT_FILE.write_text(html)
    print(f"\nBuilt {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
