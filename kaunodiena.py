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

# urls = [element['href'] for element in ResultsSet]
article_names = [element.text for element in ResultsSet]

data_table = pd.DataFrame()
data_table['article_name'] = article_names

data_table.to_csv('kaunodiena.csv', sep=';')

driver.close()