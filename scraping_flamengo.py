import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

r = requests.get('https://www.flamengo.com.br/elencos/elenco-profissional')
base_url='https://fla-bucket-s3-us.s3.amazonaws.com/public/images/players/'
url_to_parse = "https://www.flamengo.com.br/elencos/elenco-profissional"

# for beautiful soup
from bs4 import BeautifulSoup
bs = BeautifulSoup(r.content)
imgs = bs.findAll('img')
for img in imgs:
    src = img.attrs['src']
    if src.startswith(base_url):
        src = (base_url+src)
        print(src)
imgs = bs.findAll('img')[5:32]
#In order to get only the players name, I had to limit from 5:32 line, as writen above
for img in imgs:
    alt = img.attrs['alt']
    if not alt.startswith(base_url):
        alt = (base_url+alt)
        #It was not clear during the test if I needed to return only the players name or the entire line. However, here I decide to bring only their names.
        alt = alt[64:]
        print(alt)

response = requests.get(url_to_parse)
response_text = response.text
soup = BeautifulSoup(response_text, 'lxml')
#Different from the code related to the players name, here , about their position, I brough the entire line. 
span = soup.find_all("span",class_="see-more font-weight-bold text-decoration-none text-white")
for item in span:
    print(item)

