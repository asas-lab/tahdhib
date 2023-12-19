import requests
from bs4 import BeautifulSoup
import time


def scrape_web(page_urls):
    all_text = []

    for url in page_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        text = soup.get_text().replace('\n', ' ')
        all_text.append(text)

        time.sleep(1)  

    return all_text


page_urls = [
    'https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D9%84%D8%BA%D8%A9_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9',
    'https://www.arabtrvl.com/vb/t3065.html',
    'https://www.aljazeera.net/midan/miscellaneous/education/2022/9/29/%D8%A3%D8%B3%D9%87%D9%84-%D9%84%D8%BA%D8%A7%D8%AA-%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D8%A9-%D9%84%D9%84%D9%85%D8%A8%D8%AA%D8%AF%D8%A6%D9%8A%D9%86-%D9%83%D9%8A%D9%81-%D8%AA%D8%A8%D8%AF%D8%A3'
]

scraped_data = scrape_web(page_urls)

# Print and save scraped data
with open('scraped_data.txt', 'w', encoding='utf-8') as file:
    for page_text in scraped_data:
        print(page_text)
        print("--------------------------------------------------")
        file.write(page_text + '\n--------------------------------------------------\n')
