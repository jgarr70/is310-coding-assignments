from bs4 import BeautifulSoup
import requests
import cloudscraper
import csv

scraper = cloudscraper.create_scraper()

response = scraper.get("https://rickriordan.com/characters/")



# url = "https://rickriordan.com/characters/"

# response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)
characters = soup.find_all("div", class_="character")

pj_characters = []

for character in characters:
    name = character.get_text(separator='/n', strip=True)
    link = character.find('a')['href']    
    char_res = requests.get(link, timeout=10)
    char_soup = BeautifulSoup(char_res.text, "html.parser")

    quote = char_soup.find("p", class_="quote")
    
    if quote:
        words = quote.get_text(strip=True)
        pj_characters.append({'name': {name}, 'link': {link}, 'quote': {words}})
    else:
        pj_characters.append({'name': {name}, 'link': {link}, 'quote': {"No quote found"}})




with open('pjcharacters.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['name', 'link', 'quote'])
    for character in pj_characters:
        writer.writerow([character['name'], character['link'], character['quote']])
