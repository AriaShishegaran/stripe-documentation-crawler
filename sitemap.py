import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from urllib.parse import urljoin

async def fetch_xml(url, session):
    """Fetch XML content asynchronously from a given URL using aiohttp and parse it with ElementTree."""
    try:
        async with session.get(url) as response:
            text = await response.text()
            return ET.fromstring(text)
    except Exception as e:
        print(f"Error fetching or parsing XML from {url}: {str(e)}")
        return None

async def fetch_sitemap_urls(sitemap_url, session):
    """Parse sitemap XML to extract URLs of further sitemaps or page URLs."""
    print(f"Fetching URLs from sitemap: {sitemap_url}")
    sitemap = await fetch_xml(sitemap_url, session)
    if sitemap is None:
        return []
    namespaces = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [loc.text for loc in sitemap.findall('.//sitemap:loc', namespaces)]
    return urls

async def fetch_and_process_all_urls(sitemap_url, session, all_urls):
    """Recursively fetch and process sitemap URLs and collect all final page URLs."""
    try:
        urls = await fetch_sitemap_urls(sitemap_url, session)
        for url in urls:
            if url.endswith('.xml'):
                # Recurse into the sitemap if the URL points to another sitemap file
                await fetch_and_process_all_urls(url, session, all_urls)
            else:
                all_urls.add(url)
                print(f"Added URL: {url}")
    except Exception as e:
        print(f"Error processing sitemap {sitemap_url}: {str(e)}")

def generate_xml(all_urls):
    """Generate a well-structured XML file from a set of URLs."""
    print("Generating final XML file.")
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in sorted(all_urls):
        url_elem = ET.SubElement(root, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = url
    return ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')

async def main(sitemap_url):
    """Main function to orchestrate the entire sitemap fetching and processing."""
    async with aiohttp.ClientSession() as session:
        all_urls = set()
        await fetch_and_process_all_urls(sitemap_url, session, all_urls)
        xml_content = generate_xml(all_urls)
        with open("sitemap_results.xml", "w", encoding="utf-8") as file:
            file.write(xml_content)
        print("Sitemap processing completed and saved to 'sitemap_results.xml'.")

# URL of the initial sitemap
initial_sitemap_url = "https://stripe.com/sitemap/sitemap.xml"

# Start the asynchronous sitemap crawling process
asyncio.run(main(initial_sitemap_url))
