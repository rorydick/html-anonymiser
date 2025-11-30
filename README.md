# HTML Anonymizer

A lightweight Python tool that strips visible text from HTML files and replaces it with placeholders, while preserving the entire document structure, attributes, CSS, and Scripts.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Python 3](https://img.shields.io/badge/python-3.6+-blue.svg)

**Useful for:**
* **Wireframing:** Instantly turning a finished website back into a layout template.
* **Privacy:** Sanitizing HTML pages containing sensitive data before sharing them for debugging or analysis.
* **Design Analysis:** Visualizing the structure and weight of a page without being distracted by the content.

## Features

- **Smart Filtering:** Only replaces visible text. Ignores `<script>`, `<style>`, `<meta>`, `<link>`, and other non-visible tags to ensure the page still functions and looks correct.
- **Structure Preservation:** Keeps all HTML tags, classes, IDs, and attributes intact.
- **Custom Placeholders:** Allows you to define your own placeholder text (e.g., "REDACTED", "LOREM", etc.).
- **Whitespace Handling:** Preserves original whitespace and formatting around text nodes.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/html-anonymizer.git
   cd html-anonymizer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   *(Note: This project relies on `beautifulsoup4` and `html5lib`)*

## Usage

Run the script from the command line, providing the input HTML file and the desired output path.

### Basic Usage
Replaces all visible text with the default word "placeholder".

```bash
python anonymise_html.py input.html output.html
```

### Custom Placeholder
Use the `-p` flag to specify your own replacement text.

```bash
python anonymise_html.py sensitive_data.html safe_version.html -p "CONFIDENTIAL"
```

## How It Works

The script parses the HTML using `BeautifulSoup` with the `html5lib` parser. It iterates through every text node in the document tree and checks its parent tags.

If the text belongs to a structural or invisible tag (like `<script>` or `<head>`), it is left alone. If it is visible content, a regular expression (`\b\w+\b`) identifies words and replaces them with your chosen placeholder, maintaining the rough "shape" of the original text blocks.

## Example

**Input:**
```html
<div class="user-profile">
  <h1>John Doe</h1>
  <p>Email: john.doe@example.com</p>
</div>
```

**Output:**
```html
<div class="user-profile">
  <h1>placeholder placeholder</h1>
  <p>placeholder: placeholder.placeholder@placeholder.placeholder</p>
</div>
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
