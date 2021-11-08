from html.parser import HTMLParser

# List of the menu to parse through
ruoka=[]
class MyHTMLParser(HTMLParser):

    def handle_data(self, data):        
        if len(data) > 5: 
            ruoka.append(data)

# Not able to get html source code from a php website, so for now only accepting pasted text.
parser = MyHTMLParser()
parser.feed('<h2>Ravintola Aurinkosalissa 8.11. - 14.11. </h2><p><b>Maanantai</b></p><p>Kalapyörykät, tilli-kermaviilikastike ja perunat<b> G, L</b></p><p>Kasvis-papukroketit,tilli-kermaviilikastike ja perunat<b> G, L</b></p><p>Herkkusienikeittoa<b> G, L</b></p><p><b>Tiistai</b></p><p>Kirkasta kalkkunakeittoa<b> G, M</b></p><p>Parsakaali-papuvuokaa<b> G, M</b></p><p>Tomaatti-chili-korianterikeitto<b> G, M</b></p><p>Mansikkakiisseliä<b> M, G</b></p><p><b>Keskiviikko</b></p><p>Kebabkiusausta<b> G, L</b></p><p>Soija-kasviskiusaus<b> G, L</b></p><p>Punajuurisosekeittoa <b> L, G</b></p><p><b>Torstai</b></p><p>Hunajainen timjami-broileripata ja täysjyväriisiä<b> G, L</b></p><p>Chili sin carne nyhtökaurasta ja täysjyväriisiä<b> M</b></p><p>Vihreä parsakeitto<b> G, L</b></p><p><b>Perjantai</b></p><p>Curry-paprika-possupataa, keitetyt perunat<b> G, L</b></p><p>Tomaatti-tofupastaa ja vegaanista juustoraastetta<b> M</b></p><p>Inkivääri-porkkanasosekeittoa<b> G, L</b></p>')
ruoka.append(" ")

viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai"]

for i in range(0,len(ruoka)-1):
    if ruoka[i] in viikonpaivat:
        print(ruoka[i] + "\n")
        print(ruoka[i+1])
        print(ruoka[i+2])
        print(ruoka[i+3])
        if ruoka[i+4] not in viikonpaivat:
            print(ruoka[i+4] + "\n")
        else: 
            print("\n")
        
        
