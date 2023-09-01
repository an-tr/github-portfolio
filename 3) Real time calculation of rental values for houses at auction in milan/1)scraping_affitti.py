from bs4 import BeautifulSoup
import requests
import csv



#1) making link for each zone in milan in the category RENT 
links=[
'https://www.immobiliare.it/affitto-case/milano/corvetto-rogoredo/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/precotto-turro/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/pasteur-rovereto/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/ripamonti-vigentino/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/citta-studi-susa/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/solari-washington/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/san-siro-trenno/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/porta-romana-cadore-montenero/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/porta-venezia-indipendenza/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/fiera-sempione-city-life-portello/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/zona-navigli/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/garibaldi-moscova-porta-nuova/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/quadronno-palestro-guastalla/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/genova-ticinese/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/arco-della-pace-arena-pagano/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/centrale-repubblica/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/bicocca-niguarda/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/cenisio-sarpi-isola/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/affori-bovisa/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/viale-certosa-cascina-merlata/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/bisceglie-baggio-olmi/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/bande-nere-inganni/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/forlanini/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/famagosta-barona/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/maggiolina-istria/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/abbiategrasso-chiesa-rossa/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/udine-lambrate/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/porta-vittoria-lodi/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/ponte-lambro-santa-giulia/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/cimiano-crescenzago-adriano/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/napoli-soderini/?criterio=rilevanza&pag=',
'https://www.immobiliare.it/affitto-case/milano/centro/?criterio=rilevanza&pag='
]
tags_raw=[
'corvetto-rogoredo',
'precotto-turro',
'pasteur-rovereto',
'ripamonti-vigentino',
'citta-studi-susa',
'solari-washington',
'san-siro-trenno',
'porta-romana-cadore-montenero',
'porta-venezia-indipendenza',
'fiera-sempione-city-life-portello',
'zona-navigli',
'garibaldi-moscova-porta-nuova',
'quadronno-palestro-guastalla',
'genova-ticinese',
'arco-della-pace-arena-pagano',
'centrale-repubblica',
'bicocca-niguarda',
'cenisio-sarpi-isola',
'affori-bovisa',
'viale-certosa-cascina-merlata',
'bisceglie-baggio-olmi',
'bande-nere-inganni',
'forlanini',
'famagosta-barona',
'maggiolina-istria',
'abbiategrasso-chiesa-rossa',
'udine-lambrate',
'porta-vittoria-lodi',
'ponte-lambro-santa-giulia',
'cimiano-crescenzago-adriano',
'napoli-soderini',
'centro'
]

#2) opening the file csv to save the data
with open('houses_rent_raw.csv',mode='w')  as file:
    writer= csv.writer(file)
    writer.writerow(['Name','Zone','Price','Surface'])
    print('lunghezza zone',len(tags_raw))

#3) taking from each zone the name, the surface and the price of the rent of each house 
    y=0
    while y < len(tags_raw):
        print('AVANZAMANTO: ',round(y*100/(len(tags_raw)-1)),'%')
        for x in range(1,30):
            
            html_text=requests.get(links[y]+ str(x)).text
            soupraw= BeautifulSoup(html_text,'lxml')
            soupfinal=soupraw.find_all('div',{'class':'nd-mediaObject__content in-card__content in-realEstateListCard__content'})

            for soup in soupfinal:
                
                name_raw=soup.find('a',class_="in-card__title")
                price_raw=soup.find('li',{'class':"nd-list__item in-feat__item in-feat__item--main in-realEstateListCard__features--main"})
                surface_raw=soup.find('li',{'class':"nd-list__item in-feat__item",'aria-label':"superficie"})

                #4) brief cleaning
                if(name_raw is not None and price_raw is not None and surface_raw is not None):
                    
                    name=name_raw.text.replace('à','a').replace('è','e').replace('é','e').replace('ì','i').replace('ò','o').replace('ù','u').replace('m²','').replace('ö','o')
                    tag=tags_raw[y]
                    price=price_raw.text.replace('/mese','').replace('€','').replace('.','').replace(' ','')
                    surface=surface_raw.text.replace('m²','').replace('.','')
                    
                #5) saving in the file csv
                    array=[]
                    array.append(name)
                    array.append(tag)
                    array.append(price)
                    array.append(surface)
                    writer.writerow(array)
        y+=1
                
            

    
    
   
    
   