import cloudscraper
from bs4 import BeautifulSoup


scraper = cloudscraper.create_scraper()

response = scraper.get("https://lotr.fandom.com/wiki/Category:Canon_characters_in_The_Rings_of_Power")
soup = BeautifulSoup(response.text, "html.parser")
characters = soup.find_all('a', class_='category-page__member-link')

response.raise_for_status()
print(response.status_code)

for character in characters:
    print(character.get_text())