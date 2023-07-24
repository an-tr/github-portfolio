import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#name of the citis for the analysis
cities = {
    'AG' : 'Agrigento',
    'AL' : 'Alessandria',
    'AN' : 'Ancona',
    'AO' : 'Aosta',
    'AR' : 'Arezzo',
    'AP' : 'Ascoli-Piceno',
    'AT' : 'Asti',
    'AV' : 'Avellino',
    'BA' : 'Bari',
    'BT' : 'Barletta',
    'BL' : 'Belluno',
    'BN' : 'Benevento',
    'BG' : 'Bergamo',
    'BI' : 'Biella',
    'BO' : 'Bologna',
    'BZ' : 'bolzano-bozen',
    'BS' : 'Brescia',
    'BR' : 'Brindisi',
    'CA' : 'Cagliari',
    'CL' : 'Caltanissetta',
    'CB' : 'Campobasso',
    'CI' : 'Carbonia',
    'CE' : 'Caserta',
    'CT' : 'Catania',
    'CZ' : 'Catanzaro',
    'CH' : 'Chieti',
    'CO' : 'Como',
    'CS' : 'Cosenza',
    'CR' : 'Cremona',
    'KR' : 'Crotone',
    'CN' : 'Cuneo',
    'EN' : 'Enna',
    'FM' : 'Fermo',
    'FE' : 'Ferrara',
    'FI' : 'Firenze',
    'FG' : 'Foggia',
    'FC' : 'forli',
    'FR' : 'Frosinone',
    'GE' : 'Genova',
    'GO' : 'Gorizia',
    'GR' : 'Grosseto',
    'IM' : 'Imperia',
    'IS' : 'Isernia',
    'SP' : 'La-Spezia',
    'AQ' : 'LAquila',
    'LT' : 'Latina',
    'LE' : 'Lecce',
    'LC' : 'Lecco',
    'LI' : 'Livorno',
    'LO' : 'Lodi',
    'LU' : 'Lucca',
    'MC' : 'Macerata',
    'MN' : 'Mantova',
    'MS' : 'Massa',
    'MT' : 'Matera',
    'ME' : 'Messina',
    'MI' : 'Milano',
    'MO' : 'Modena',
    'MB' : 'Monza',
    'NA' : 'Napoli',
    'NO' : 'Novara',
    'NU' : 'Nuoro',
    'OT' : 'Olbia',
    'OR' : 'Oristano',
    'PD' : 'Padova',
    'PA' : 'Palermo',
    'PR' : 'Parma',
    'PV' : 'Pavia',
    'PG' : 'Perugia',
    'PU' : 'Pesaro',
    'PE' : 'Pescara',
    'PC' : 'Piacenza',
    'PI' : 'Pisa',
    'PT' : 'Pistoia',
    'PN' : 'Pordenone',
    'PZ' : 'Potenza',
    'PO' : 'Prato',
    'RG' : 'Ragusa',
    'RA' : 'Ravenna',
    'RC' : 'Reggio-di-Calabria',
    'RE' : 'Reggio-nellemilia',
    'RI' : 'Rieti',
    'RN' : 'Rimini',
    'RM' : 'Roma',
    'RO' : 'Rovigo',
    'SA' : 'Salerno',
    'SS' : 'Sassari',
    'SV' : 'Savona',
    'SI' : 'Siena',
    'SR' : 'Siracusa',
    'SO' : 'Sondrio',
    'TA' : 'Taranto',
    'TE' : 'Teramo',
    'TR' : 'Terni',
    'TO' : 'Torino',
    'OG' : 'Ogliastra',
    'TP' : 'Trapani',
    'TN' : 'Trento',
    'TV' : 'Treviso',
    'TS' : 'Trieste',
    'UD' : 'Udine',
    'VA' : 'Varese',
    'VE' : 'Venezia',
    'VB' : 'san-bernardino-verbano',
    'VC' : 'Vercelli',
    'VR' : 'Verona',
    'VV' : 'Vibo-Valentia',
    'VI' : 'Vicenza',
    'VT' : 'Viterbo',
}

sigle=list(cities.keys())


#preparing the driver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

actions = ActionChains(driver)
x_coord = 297
y_coord = 755
            
actions.move_by_offset(x_coord, y_coord).click().perform()


#opening file
with open('politics_raw.csv',mode='w')  as file:
    writer= csv.writer(file)
    writer.writerow(['city','year','party','tot_invest','amministration_invest','social_invest','environment_invest','transport_invest','education_invest','culture_invest','sport_invest','tourism_invest','economic_invest','sevice_invest','police_invest','justice_invest'])
    

    #3) scraping of all pages to find all the investments for all the categories and the ruling party for each year
    y=0
    len_cities=len(cities)
    

    while y < len_cities:
        print('AVANZAMANTO: ',round(y*100/(len_cities)),'%')
        for x in range(2005,2015):
            
            
            link='http://storico.openbilanci.it/bilanci/'+cities[sigle[y]].lower()+'-comune-'+sigle[y].lower()+'/spese/dettaglio?year='+str(x)+'&type=consuntivo&cas_com_type=cassa'
            print(link)
            
            driver.get(link)
            time.sleep(1)
            num_party=0
            for i in range(1,20):
                try:
                    partitoraw=driver.find_element(By.XPATH, "//*[@id='main-content']/div[1]/div[5]/div/div/div/div/div[1]/div/div/div[1]/div["+str(i)+"]")
                    partiti=driver.find_element(By.XPATH, "//*[@id='main-content']/div[1]/div[5]/div/div/div/div/div[1]/div/div/div[1]/div["+str(i)+"]/div[2]/div[2]").text
                    partitoclasse=partitoraw.get_dom_attribute("class")
                    
                except:
                    break
                
                if partitoclasse == 'visup-span-descr visup-span-descr-highlighted':
                     
                     num_party=num_party+1
                     partito=partiti

           
           
            
            
            if num_party == 1:
                party=partito
            else:
                party='more_party'

            city=cities[sigle[y]].lower()
            year=x

            

            actions.move_by_offset(0, 0).click().perform()
             
            


            
            #taking values
            try:
                tot_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni']/div[1]/div[4]/div[2]/p/strong/span").text
                amministration_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-amministrazione']/div[1]/div[4]/div[2]/p/strong/span").text
                social_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-sociale']/div[1]/div[4]/div[2]/p/strong/span").text
                environment_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-territorio-e-ambiente']/div[1]/div[4]/div[2]/p/strong/span").text
                transport_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-viabilita-e-trasporti']/div[1]/div[4]/div[2]/p/strong/span").text
                education_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-istruzione']/div[1]/div[4]/div[2]/p/strong/span").text
                culture_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-cultura']/div[1]/div[4]/div[2]/p/strong/span").text
                sport_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-sport']/div[1]/div[4]/div[2]/p/strong/span").text
                tourism_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-turismo']/div[1]/div[4]/div[2]/p/strong/span").text
                economic_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-sviluppo-economico']/div[1]/div[4]/div[2]/p/strong/span").text
                sevice_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-servizi-produttivi']/div[1]/div[4]/div[2]/p/strong/span").text
                police_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-polizia-locale']/div[1]/div[4]/div[2]/p/strong/span").text
                justice_invest=driver.find_element(By.XPATH, "//*[@id='heading-consuntivo-spese-cassa-spese-somma-funzioni-giustizia']/div[1]/div[4]/div[2]/p/strong/span").text
            except:
                pass 

                
            # save the values into the csv file        
            array=[]
            array.append(city)
            array.append(year)
            array.append(party)
            array.append(tot_invest.replace('€',''))
            array.append(amministration_invest.replace('€',''))
            array.append(social_invest.replace('€',''))
            array.append(environment_invest.replace('€',''))
            array.append(transport_invest.replace('€',''))
            array.append(education_invest.replace('€',''))
            array.append(culture_invest.replace('€',''))
            array.append(sport_invest.replace('€',''))
            array.append(tourism_invest.replace('€',''))
            array.append(economic_invest.replace('€',''))
            array.append(sevice_invest.replace('€',''))
            array.append(police_invest.replace('€',''))
            array.append(justice_invest.replace('€',''))
            writer.writerow(array)
                    
        y+=1
        