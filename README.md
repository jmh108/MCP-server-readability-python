# Mozilla Readability Parser MCP Server (Python)

A Python implementation of the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) server that extracts and transforms webpage content into clean, LLM-optimized Markdown.

## Table of Contents
- [Features](#features)
- [Why Not Just Fetch?](#why-not-just-fetch)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Tool Reference](#tool-reference)
- [Dependencies](#dependencies)
- [License](#license)

## Features
- Removes ads, navigation, footers and other non-essential content
- Converts clean HTML into well-formatted Markdown
- Handles errors gracefully
- Optimized for LLM processing
- Lightweight and fast

## Why Not Just Fetch?
Unlike simple fetch requests, this server:
- Extracts only relevant content using Readability algorithm
- Eliminates noise like ads, popups, and navigation menus
- Reduces token usage by removing unnecessary HTML/CSS
- Provides consistent Markdown formatting for better LLM processing
- Handles complex web pages with dynamic content

## Installation

1. Clone the repository:
```bash
git clone https://github.com/modelcontextprotocol/server-moz-readability-python.git
cd server-moz-readability-python
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

1. Start the server:
```bash
fastmcp run server.py
```

2. Example request:
```bash
curl -X POST http://localhost:8000/tools/extract_content \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article"}'
```

## Tool Reference

### `extract_content`
Fetches and transforms webpage content into clean Markdown.

**Arguments:**
```json
{
  "url": {
    "type": "string",
    "description": "The website URL to parse",
    "required": true
  }
}
```

**Returns:**
```json
{
  "content": "Markdown content..."
}
```

## Dependencies
- [readability-lxml](https://github.com/buriy/python-readability) - Content extraction
- [html2text](https://github.com/Alir3z4/html2text) - HTML to Markdown conversion
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - DOM parsing
- [requests](https://docs.python-requests.org/) - HTTP requests

## License
MIT License - See [LICENSE](LICENSE) for details.
