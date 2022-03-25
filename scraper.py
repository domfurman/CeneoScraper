from pydoc import resolve
from urllib import response
import requests

url = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(url)
print(response.status_code)