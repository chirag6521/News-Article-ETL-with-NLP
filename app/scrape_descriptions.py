import requests
import time
from bs4 import BeautifulSoup
import random

# List of CNN article URLs to scrape
urls = [
    "https://www.cnn.com/cnn-underscored/home/editors-favorite-sustainable-products?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/gifts/best-mothers-day-gifts-2023?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/fashion/mens-spring-fashion-style-guide?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/travel/amazon-travel-products?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/money/high-yield-savings-accounts?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/money/how-to-file-taxes?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/home/how-to-compost-at-home?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/reviews/mmmat-silicone-mats?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/deals/dyson-supersonic-sale-2023-04-17?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/deals/wayfair-way-day-2023-04-17?iid=CNNUnderscoredHPcontainer",
    "https://www.cnn.com/cnn-underscored/deals/best-amazon-deals-2023-04-12?iid=CNNUnderscoredHPcontainer"
]

# List of User-Agent strings
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    # Add more User-Agent strings if needed
]

def fetch_article_description(url):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_article_description(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Assuming you want to extract a specific element. Change this according to the actual HTML structure.
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title found'
    description = soup.find('meta', attrs={'name': 'description'})
    description_content = description['content'] if description else 'No description found'
    return title, description_content

for url in urls:
    html_content = fetch_article_description(url)
    if html_content:
        title, description = parse_article_description(html_content)
        print(f"Title: {title}")
        print(f"Description: {description}")
    time.sleep(2)  # Wait for 2 seconds between requests
