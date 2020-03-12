# Obtención de proxys y user agents automatizada, utiles en el proceso de web scraping

import requests

from bs4    import BeautifulSoup
from urllib import request

uri_prox  = "https://free-proxy-list.net/"
uri_users = "https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/"

prox  = requests.get(uri_prox).text
users = requests.get(uri_users).text

soup_prox  = BeautifulSoup(prox ,'lxml')
soup_users = BeautifulSoup(users,'lxml')

taged_prox_ls = soup_prox.findChild("tbody")
listed_prox   = [tag for tag in taged_prox_ls.find_all("tr")]

prox_table  = {}
count       = 0

for Result in listed_prox:
    listed_props = Result.find_all("td")
    IP      =  listed_props[0].get_text()
    PORT    =  listed_props[1].get_text()
    COUNTRY =  listed_props[3].get_text()
    P_TYPE  =  listed_props[4].get_text()
    HTTP    =  listed_props[6].get_text()
    
    proxie  =  {
        "IP"  : IP,
        "PORT": PORT,
        "COUNTRY": COUNTRY,
        "P_TYPE": P_TYPE,
        "HTTPS": HTTP,
    }
    prox_table.update({"PROXY"+ str(count) : proxie})
    count += 1

taged_usrs_ls = soup_users.findChild("tbody")
listed_usrs   = [taged_usr for taged_usr in taged_usrs_ls.find_all("tr")]
users = [user.findChild("td").text for user in listed_usrs]