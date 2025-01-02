from fastmcp import FastMCP
from readability.readability import Document as ReadabilityDocument
import requests
from bs4 import BeautifulSoup
import html2text

# Create MCP server
mcp = FastMCP("Readability Server")

@mcp.tool()
def parse(url: str) -> dict:
    """Fetch and transform webpage content into clean Markdown with metadata"""
    try:
        # Fetch webpage content
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML with readability
        doc = ReadabilityDocument(response.text)
        content_html = doc.summary()
        title = doc.short_title()
        
        # Extract metadata
        soup = BeautifulSoup(response.text, 'lxml')
        excerpt = soup.find('meta', attrs={'name': 'description'})
        byline = soup.find('meta', attrs={'name': 'author'})
        site_name = soup.find('meta', attrs={'property': 'og:site_name'})
        
        # Convert to markdown
        markdown = html2text.html2text(content_html)
        
        return {
            "title": title,
            "content": markdown,
            "metadata": {
                "excerpt": excerpt.get('content') if excerpt else None,
                "byline": byline.get('content') if byline else None,
                "siteName": site_name.get('content') if site_name else None
            }
        }
    except Exception as e:
        return {"error": f"Error processing URL: {str(e)}"}

if __name__ == "__main__":
    # Run in development mode
    import os
    os.system("fastmcp dev server.py")
