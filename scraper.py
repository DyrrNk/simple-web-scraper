import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h3')

for headline in headlines[:5]:
    print(headline.text.strip())
