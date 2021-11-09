""" PALMIA: 
# Yksittäinen ruokaitemi, HTML koodista
class="meal-name invidual-restaurant-meal-name"

# Päivämäärän merkintä
data-date="2021-11-9"

# Suomenkielinen, ruotsiksi id="3"
data-language-id="2"

# Jokaisessa Kasvislounaassa sekä Lounas ja Lounaan Lisukkeet
class="invidual-restaurant-meal-paragraph"
    #Pelkkä "Lounas" teksti
    class="meal-of-day invidual-restaurant-meal-of-day"

data-meal="UyQ-KpQHSUKn_ccO_dpEIw" """

import requests
import bs4
from datetime import datetime

def päivän_ruokalista():

    # Kerro nykyinen päivä numerona 0 maanantai - 6 sunnuntai
    päivä = datetime.today().weekday()
    #print(päivä)
    
    """ koulu = str(input("Kirjoita koulun nimi: ")).lower()
    koulu = koulu.replace(" ", "-") """
    

    res = requests.get(f"https://ruoka.palmia.fi/fi/ravintola/koulu/alppilan-lukio/")
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Päivän ruoka listaksi, josta korjataan ylimääräiset välit pois

    ruoka= []
    
    d = soup.select(".menu-list-day.invidual-restaurant-menu-list-day")
    s = (d[päivä].getText())
    ruoka.append(s)
    ruoka = [s.replace("\n\n\n\n\n", "\n") for s in ruoka]
    print(ruoka[0])

päivän_ruokalista()

