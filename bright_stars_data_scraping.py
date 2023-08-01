from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


# URL para coleta de dados
bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(bright_stars_url)

# Obtenha a Página
page = requests.get(bright_stars_url)
print(page)

# Analise a Página
soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
#table_rows = star_table.find_all('tr')
#table_rows = star_table.find_all('t')
#table_rows = star_table.find_all('tt')
for tr in table_rows:
    #td = tr.find_all('tt')
    #td = tr.find_all('tr')
    #td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

# Converta para CSV
headers = ['Star_name','Distance','Mass','Radius','Luminosity']    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=headers)
print(df2)

df2.to_csv('bright_stars.csv', index=True, index_label="id")
