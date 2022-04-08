from pydoc import resolve
from urllib import response
import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
stars = opinion.select_one("span.user-post__score-count").get_text().strip()
content = opinion.select_one("div.user-post__text").get_text().strip()
useful = opinion.select_one('span[id^="votes-yes"]').get_text().strip()
useless = opinion.select_one('span[id^="votes-no"]').get_text().strip()
publish_date = opinion.select_one('span.user-post__published > time:nth-child(1) ["datetime"]').get_text().strip()
purchase_date = opinion.select_one('span.user-post__published > time:nth-child(2) ["datetime"]').get_text().strip()

#print(type(opinion_id))
print((publish_date))