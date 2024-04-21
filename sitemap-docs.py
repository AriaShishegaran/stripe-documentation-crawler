import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

async def fetch_content(url, session):
    try:
        async with session.get(url) as response:
            content = await response.text()
            print(f"Content fetched for {url} - Length: {len(content)}")
            return content
    except Exception as e:
        print(f"Failed to fetch {url}: {str(e)}")
        return None

async def fetch_sitemap_urls(sitemap_url, session):
    content = await fetch_content(sitemap_url, session)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        urls = [loc.text for loc in soup.find_all('loc')]
        return urls
    return []

def parse_html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Updated to a more general selector that should be adjusted based on actual page structure
    content_elements = soup.find('article', {'id': 'content'})
    if not content_elements:
        print("Content element not found.")
        return "Content not found."

    markdown = []
    for element in content_elements.descendants:
        if element.name == 'h1':
            markdown.append(f"# {element.get_text().strip()}\n")
        elif element.name == 'h2':
            markdown.append(f"## {element.get_text().strip()}\n")
        elif element.name == 'p':
            markdown.append(f"{element.get_text().strip()}\n")
        elif element.name == 'li':
            markdown.append(f"- {element.get_text().strip()}\n")
        elif element.name == 'a' and element.get('href'):
            text = element.get_text().strip()
            href = element['href']
            markdown.append(f"[{text}]({href})\n")

    markdown_text = '\n'.join(markdown)
    print(f"Generated Markdown - Length: {len(markdown_text)}")
    return markdown_text if markdown else "Content not found."

def save_content_to_file(url, markdown_content):
    parsed_url = urlparse(url)
    directory = os.path.join('stripe_docs', parsed_url.netloc, os.path.dirname(parsed_url.path.strip('/')))
    filename = os.path.join(directory, os.path.basename(parsed_url.path) + '.md')
    os.makedirs(directory, exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"Saved Markdown to {filename}, Content Length: {len(markdown_content)}")

async def process_url(url, session):
    print(f"Processing {url}")
    html_content = await fetch_content(url, session)
    if html_content:
        markdown_content = parse_html_to_markdown(html_content)
        save_content_to_file(url, markdown_content)

async def main(sitemap_url):
    async with aiohttp.ClientSession() as session:
        urls = await fetch_sitemap_urls(sitemap_url, session)
        tasks = [process_url(url, session) for url in urls]
        await asyncio.gather(*tasks)
        print("All tasks completed.")

sitemap_url = "https://docs.stripe.com/sitemap.xml"
asyncio.run(main(sitemap_url))
