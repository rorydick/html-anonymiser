#!/usr/bin/env python3
import sys, argparse, re
from bs4 import BeautifulSoup, NavigableString, Comment
import html5lib

TAGS_IGNORE = {'script','style','head','title','noscript','meta','link','iframe'}
PLACEHOLDER = "placeholder"

word_rx = re.compile(r'\b\w+\b', flags=re.UNICODE)

def generate_placeholder_text(text, placeholder_word=PLACEHOLDER):
    return word_rx.sub(lambda m: placeholder_word, text)

def is_visible_text(node):
    if not isinstance(node, NavigableString): return False
    if isinstance(node, Comment): return False
    parent = node.parent
    return parent and parent.name and parent.name.lower() not in TAGS_IGNORE

def anonymize_html_content(html: str, placeholder_word=PLACEHOLDER) -> str:
    soup = BeautifulSoup(html, 'html5lib')
    for text_node in soup.find_all(string=True):
        if is_visible_text(text_node):
            orig = str(text_node)
            stripped = orig.strip()
            if stripped:
                repl = generate_placeholder_text(stripped, placeholder_word)
                # preserve surrounding whitespace
                new = orig.replace(stripped, repl)
                text_node.replace_with(new)
    # Render full document
    return soup.decode()

def main():
    p = argparse.ArgumentParser(description="Anonymize visible text only, preserving CSS/JS.")
    p.add_argument("input_file")
    p.add_argument("output_file")
    p.add_argument("-p","--placeholder", default=PLACEHOLDER)
    args = p.parse_args()

    try:
        html = open(args.input_file, encoding='utf‑8').read()
    except Exception as e:
        sys.exit(f"Error reading input: {e}")

    result = anonymize_html_content(html, args.placeholder)

    try:
        with open(args.output_file, 'w', encoding='utf‑8') as f:
            f.write(result)
    except Exception as e:
        sys.exit(f"Error writing output: {e}")

    print("[+] Done.")

if __name__=="__main__":
    main()
