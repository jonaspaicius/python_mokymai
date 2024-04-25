import selenium
import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time # dėl sleep komandos

opcijos = Options()
opcijos.add_argument('--incognito')

driver = uc.Chrome(options=opcijos)
url = "https://www.kaunodiena.lt"

driver.get(url)
time.sleep(10)

source = driver.page_source # pasiima puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') # teoriškai išparsinome puslapio html
ResultsSet = bs.find_all('a', {'class':'articles-list-title'})

urls = [element['href'] for element in ResultsSet]
article_names = [element.text for element in ResultsSet]

article_texts = []

for url in urls[:2]:
    driver.get("https://www.kaunodiena.lt/"+url)
    time.sleep(10)
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    ResultsSet = bs.find_all('span', {'itemprop':'articleBody'})
    tekstas = ''
    for element in ResultsSet:
        ResultsSubSet = element.find_all('p')
        for pastraipa in ResultsSubSet:
            tekstas = tekstas + ' ' + str(pastraipa)
    article_texts.append(tekstas)

article_texts_table = pd.DataFrame()

# article_texts_table['article_name'] = article_names
# article_texts_table['url'] = urls
article_texts_table['text'] = article_texts

article_texts_table.to_csv('kaunodienatekstai.csv', sep='|')

driver.close()