# ===SKELBIMAS===
# linkas,
# adresas
# kaina
# kaina už 1 kv metrą

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
url = "https://www.aruodas.lt/butai/puslapis/2/"

driver.get(url)
time.sleep(15)

source = driver.page_source # pasiima puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') # teoriškai išparsinome puslapio html
# ResultsSet = bs.find_all('div', {'class':'advert-flex'})
ResultsSet = bs.find_all('div', {'list-adress-v2'})

for skelbimas in ResultsSet:
    try:
        # addres_element  = skelbimas.find('div', {'class':'list-adress-v2'})
        # tag = addres_element.find('h3').find('a', href=True)
        tag = skelbimas.find('h3').find('a', href=True)
        linkas = tag['href']
        # tekstą galima pasiekti ir per 
        # .contents atributą
        tekstas = tag.contents #jums gražina list objektą su teksto gabalais
        f = ''
        for i in tekstas:
            f = f + str(i).strip() # str - kad garantuotai būtų tekstas
        adresas = f.replace('<br/>', ', ')
        kaina = skelbimas.find('div', {'class':'price'}).find('span', {'class':'list-item-price-v2'}).text.strip()
        kaina_m2 = skelbimas.find('div', {'class':'price'}).find('span', {'class':'price-pm-v2'}).text.strip().replace(' ','')[:-4]+' €/m²'
        
        # tuo tarpu .text gražina contents tekstą kaip vientisą
        # tekstas = tag.text.strip() # string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
        print("====SKELBIMAS====")
        print(linkas)
        print(adresas)
        print(kaina)
        print(kaina_m2)
    except:
        pass
                                     
driver.close()