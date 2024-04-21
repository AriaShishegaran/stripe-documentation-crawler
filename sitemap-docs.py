import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup, NavigableString, Tag
from datetime import datetime
from urllib.parse import urlparse, unquote
import hashlib
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
URL_DATA_FILE = 'url_data.json'
MARKDOWN_FOLDER = 'markdown_files'

# Util functions
def load_url_data():
    """Load URL data from a local JSON file."""
    try:
        with open(URL_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning("URL data file not found. Creating a new one.")
        return {}

def save_url_data(data):
    """Save URL data to a local JSON file."""
    with open(URL_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)
    logging.info("URL data saved successfully.")

def url_to_filepath(url):
    """Convert a URL to a directory path and filename."""
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path).strip('/')
    directory = os.path.join(MARKDOWN_FOLDER, parsed_url.netloc, os.path.dirname(path))
    filename = os.path.basename(path)
    if not filename:
        filename = 'index'
    filename += '.md'
    return directory, filename

# Core functions
async def fetch_and_check_sitemap(session, sitemap_url, url_data):
    """Fetch the sitemap and identify new or changed URLs."""
    logging.info(f"Fetching sitemap from {sitemap_url}")
    async with session.get(sitemap_url) as response:
        sitemap_content = await response.text()
        soup = BeautifulSoup(sitemap_content, 'xml')
        new_data = {}

        for loc in soup.find_all('loc'):
            url = loc.text
            url_hash = hashlib.md5(url.encode()).hexdigest()  # Unique hash for URL

            if url in url_data:
                new_data[url] = url_data[url]
            else:
                new_data[url] = {'last_checked': None, 'hash': None}
                logging.info(f"New URL found: {url}")

        return new_data

async def fetch_url_content(session, url, max_retries=3, retry_delay=1):
    """Fetch content for a given URL using GET request with error handling and retries."""
    logging.info(f"Fetching content from {url}")
    retries = 0
    while retries < max_retries:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                elif response.status == 429:
                    logging.warning(f"Received status code 429 for {url}. Retrying after a delay...")
                    await asyncio.sleep(retry_delay)
                    retries += 1
                else:
                    logging.warning(f"Received status code {response.status} for {url}")
                    return None
        except aiohttp.ClientError as e:
            logging.warning(f"Error occurred while fetching {url}: {str(e)}")
            retries += 1
            if retries < max_retries:
                logging.info(f"Retrying in {retry_delay} second(s)...")
                await asyncio.sleep(retry_delay)
            else:
                logging.error(f"Max retries reached for {url}. Skipping.")
                return None

async def process_url(session, url, info):
    """Process a single URL: fetch, check for changes, save markdown."""
    logging.info(f"Processing URL: {url}")
    content = await fetch_url_content(session, url)
    if content is None:
        logging.warning(f"Skipping {url} due to fetch error.")
        return
    content_hash = hashlib.md5(content.encode()).hexdigest()

    if content_hash != info.get('hash'):
        logging.info(f"Content has changed for {url}, updating...")
        markdown = convert_html_to_markdown(content)
        directory, filename = url_to_filepath(url)
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            file.write(markdown)
        logging.info(f"Markdown saved to {filepath}")

        # Update the URL info
        info['hash'] = content_hash
        info['last_checked'] = datetime.now().isoformat()

def convert_html_to_markdown(html):
    """Convert HTML content to Markdown."""
    soup = BeautifulSoup(html, 'html.parser')
    # Remove unwanted elements
    for element in soup(["script", "style", "header", "footer", "nav"]):
        element.decompose()
    return html_to_markdown(soup)

def html_to_markdown(element, level=0):
    """Recursively convert HTML to Markdown."""
    if isinstance(element, NavigableString):
        text = element.strip()
        if not text:
            return ""
        return text + "\n\n"
    if isinstance(element, Tag):
        if element.name == 'h1':
            return f"# {element.get_text().strip()}\n\n"
        elif element.name == 'h2':
            return f"## {element.get_text().strip()}\n\n"
        elif element.name == 'h3':
            return f"### {element.get_text().strip()}\n\n"
        elif element.name == 'p':
            return f"{element.get_text().strip()}\n\n"
        elif element.name == 'ul':
            items = (html_to_markdown(li, level+1) for li in element.find_all('li', recursive=False))
            return ''.join(f"{'  ' * level}- {item}" for item in items if item.strip()) + '\n'
        elif element.name == 'ol':
            items = (html_to_markdown(li, level+1) for li in element.find_all('li', recursive=False))
            return ''.join(f"{'  ' * level}{i+1}. {item}" for i, item in enumerate(items) if item.strip()) + '\n'
        elif element.name == 'a':
            href = element.get('href', '#')
            text = element.get_text().strip()
            return f"[{text}]({href})"
        elif element.name == 'img':
            src = element.get('src', '')
            alt = element.get('alt', '')
            return f"![{alt}]({src})\n\n"
        elif element.name == 'code' or element.name == 'pre':
            return f"`{element.get_text().strip()}`"
        elif element.name == 'blockquote':
            return f"> {element.get_text().strip()}\n\n"
        elif element.name == 'table':
            headers = [th.get_text().strip() for th in element.find_all('th')]
            rows = []
            for row in element.find_all('tr'):
                cells = [td.get_text().strip() for td in row.find_all('td')]
                if cells:
                    rows.append(cells)
            table = f"| {' | '.join(headers)} |\n"
            table += f"| {' | '.join(['---'] * len(headers))} |\n"
            for row in rows:
                table += f"| {' | '.join(row)} |\n"
            return table + '\n'
        else:
            return ''.join(html_to_markdown(child, level) for child in element.children)
    return ''

async def main(sitemap_url):
    """Main function to orchestrate the fetching and updating process."""
    url_data = load_url_data()
    async with aiohttp.ClientSession() as session:
        urls_data = await fetch_and_check_sitemap(session, sitemap_url, url_data)
        tasks = [process_url(session, url, info) for url, info in urls_data.items()]
        await asyncio.gather(*tasks)
    save_url_data(urls_data)

if __name__ == "__main__":
    sitemap_url = 'https://docs.stripe.com/sitemap.xml'
    asyncio.run(main(sitemap_url))
