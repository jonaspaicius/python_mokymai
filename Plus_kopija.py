
# import undetected_chromedriver as   uc #Chrome naują langą, teoriškai neaptinkamą visokiems javascriptams,
# gaudantiems visokius webscrapperius
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.chrome.options import Options #kad galėtumėme nurodyti parametrus naršyklei
import time
import sqlite3 as S3
DB = S3.connect('sqlData2.db')
# DB.close()
C=DB.cursor()

sql1 = """ drop table if exists Autoplius """ #  sena lentele trina su visais duomenimis
C.execute(sql1)

sql = '''create table if not exists Autoplius(
Gamintojas text not null,
modelis text not null,
metai real not null,
kebulas text not null,
kaina real not null,                
galia text not null,
kW real not null,
rida real not null,
linkas text not null);'''

options = Options()
options.add_argument('--incognito')
C.execute(sql)  


driver = uc.Chrome(use_subprocess=True, suppress_welcome=True, options=options)
fp = 'Autopliuso_statistika'          #knygos pavadinimas
f = open(fp, mode='w', encoding='utf-8')        #atversta knyga 

for puslapio_sk in range(1,10):
    
    url = f'https://autoplius.lt/skelbimai/naudoti-automobiliai?fuel_id%5B35%5D=35&page_nr={puslapio_sk}/'

    driver.get(url) # užkraunam puslapį su get metodu
    source = driver.page_source #su page_source atributu gaunam puslapio kodą
    bs = BeautifulSoup(source, 'html.parser')
    ResultSet = bs.find_all('a', {'class':"announcement-item is-enhanced is-gallery is-gallery"})
    print(len(ResultSet))
    for i in ResultSet:
        linkas = ''
        gamintojas = ''
        modelis = ''
        ap = ''
        kaina = ''
        galia = ''
        rida = ''
        kW = ''
        metai = ''
        kebulas = ''
        try:
           
            try:
                linkas=i['href']
            except:
                linkas = 'Nerastas'
            try:
                gm = i.find('div', {'class':'announcement-title'}).text.strip().replace('\n',' ').split()
                gamintojas = gm[0]
                modelis = ' '.join(gm[1:])
            except:
               
                    gamintojas = 'Nerastas'
                    modelis = 'Nerastas'
            try:
                mk = i.find('div', {'class':'announcement-parameters'}).text.strip().split('\n')
                metai = int(mk[0][0:4])
                kebulas = mk[1]
            except:
                metai = -1 
                kebulas = 'Nerastas'
                
            try:
                kaina = float(i.find('div', {'class':'announcement-pricing-info'}).text.strip().replace('\n',' ').split('€')[0].replace(' ',''))
            except:
                kaina = -1
            try:
                galia = i.find('div', {'class':'announcement-parameters-block'}).find('div', {'class':'announcement-parameters has-logo'}).text.strip().replace('\n',' ').replace('    ','')
                r = galia.split()[-4:-2]
                rida = float(''.join(r))
                W = galia.split()[-6]
                try:

                    kW = (float(W))
                except:
                    kW = -2
            except:
                try:
                    galia = i.find('div', {'class':'announcement-parameters-block'}).find('div', {'class':'announcement-parameters'}).text.strip().replace('\n',' ').replace('    ','')
                    r = galia.split()[-4:-2]
                    rida = float(''.join(r))
                    W = galia.split()[-6]
                    try:
                        kW = (float(W))
                    except:
                        kW = -2
                   
                except:
                    galia = 'Nerasta'
                    rida = -1
                    kW = -2

                    
            print(gamintojas, modelis, metai, kebulas, kaina, galia, kW, rida, linkas, sep = '  ;  ')
            f.write(gamintojas+';'+modelis+';'+str(metai)+';'+kebulas+';'+str(kaina)+';'+galia+';'+str(kW)+';'+str(rida)+';'+linkas+'\n')   #str metodas skaicius isveda
            data = [(gamintojas, modelis, metai, kebulas, kaina, galia, kW, rida, linkas)]
            try:
                sql_template = '''insert into Autoplius values (?,?,?,?,?,?,?,?,?)'''
                C.executemany(sql_template, data)
                DB.commit() #įrašoma informacija  
            except Exception as ex:
                print("::SQL::",ex)
        except Exception as ex:
            print(ex)
            pass
    time.sleep(5)
f.close()
DB.close()
        
            