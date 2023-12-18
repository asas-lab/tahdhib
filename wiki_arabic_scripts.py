import requests
from bs4 import BeautifulSoup
import time


def scrape_wikipedia(start_url, max_pages=20, link_number=30):
    current_url = start_url
    all_text = []

    for _ in range(max_pages):
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        text = soup.get_text().replace('\n', ' ')
        all_text.append(text)

        links = soup.find_all('a')
        link_count = 0
        for link in links:
            href = link.get('href')
            if href and 'https://ar.wikipedia.org' in href and not href.startswith('#'):
                if '/wiki/Template:' not in href:  # Skip template pages
                    link_count += 1
                    if link_count == link_number:
                        next_page = href
                        break
        else:
            print("No more Arabic Wikipedia links found. Stopping.")
            break

        current_url = next_page
        time.sleep(1)

    return all_text

# Usage example
start_url = 'https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D9%84%D8%BA%D8%A9_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9'
scraped_data = scrape_wikipedia(start_url)

# Print scraped data
for page_text in scraped_data:
    print(page_text)
    print("--------------------------------------------------")


# Save scraped data to a text file
with open('scraped_wikipedia_data.txt', 'w', encoding='utf-8') as file:
    for page_text in scraped_data:
        file.write(page_text + '\n--------------------------------------------------\n')

