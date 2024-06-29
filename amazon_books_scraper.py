import requests
from bs4 import BeautifulSoup
import time

def scrape_amazon_books():
    url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    max_retries = 5
    retry_delay = 2  # Initial delay in seconds
    retry_attempts = 0

    while retry_attempts < max_retries:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('div', {'class': 'zg-item-immersion'})

            for product in products:
                title = product.find('div', {'class': 'p13n-sc-truncated'}).text.strip()
                price = product.find('span', {'class': 'p13n-sc-price'}).text.strip()
                rating = product.find('span', {'class': 'a-icon-alt'}).text.strip() if product.find('span', {'class': 'a-icon-alt'}) else 'N/A'

                print(f"Title: {title}")
                print(f"Price: {price}")
                print(f"Rating: {rating}")
                print("=" * 50)

            return  # Exit the function once data is successfully scraped

        elif response.status_code == 429:
            retry_attempts += 1
            print(f"Received 429 Too Many Requests. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay *= 2  # Exponential backoff

        else:
            print(f"Failed to retrieve Amazon's Best Sellers: Status code {response.status_code}")
            return

    print(f"Failed after {max_retries} retries. Consider adjusting your scraping strategy.")

if __name__ == "__main__":
    scrape_amazon_books()
