import pandas as pd

#RENT


df_rent = pd.read_csv('houses_rent_raw.csv')

# drop empty rows


for x in range(df_rent.shape[0]):
    elemento=df_rent.iloc[x, 2]
    if isinstance(elemento, str):
        if "(" in elemento :
            
            df_rent.loc[x] = pd.NA
        
       

df_rent.dropna(inplace=True)


#give a unique number for each zone
df_rent["Zone_num"] = df_rent["Zone"].map({
"corvetto-rogoredo": 1, 
"precotto-turro": 2, 
"pasteur-rovereto": 3,
"ripamonti-vigentino": 4, 
"citta-studi-susa": 5, 
"solari-washington": 6,
"san-siro-trenno": 7, 
"porta-romana-cadore-montenero": 8, 
"porta-venezia-indipendenza": 9,
"fiera-sempione-city-life-portello": 10,
"zona-navigli": 11, 
"garibaldi-moscova-porta-nuova": 12, 
"quadronno-palestro-guastalla": 13,
"genova-ticinese": 14, 
"arco-della-pace-arena-pagano": 15, 
"centrale-repubblica": 16,
"bicocca-niguarda": 17, 
"cenisio-sarpi-isola": 18, 
"affori-bovisa": 19,
"viale-certosa-cascina-merlata": 20,
"bisceglie-baggio-olmi": 21, 
"bande-nere-inganni": 22, 
"forlanini": 23,
"famagosta-barona": 24, 
"maggiolina-istria": 25, 
"abbiategrasso-chiesa-rossa": 26,
"udine-lambrate": 27, 
"porta-vittoria-lodi": 28, 
"ponte-lambro-santa-giulia": 29,
"cimiano-crescenzago-adriano": 30,
"napoli-soderini": 31, 
"centro": 32 

})

df_rent.to_csv('houses_rent.csv', index=False)


#drop the houses row when the rent is more then 3000 euro/month
df_rent = pd.read_csv('houses_rent.csv')
rows_to_remove = df_rent[df_rent['Price'] > 3000].index
df_rent = df_rent.drop(rows_to_remove) 

# saving in the file CSV
df_rent.to_csv('houses_rent.csv', index=False)











#AUCTION


df_auction = pd.read_csv('houses_auction_raw.csv')


# drop empty rows


for x in range(df_auction.shape[0]):

    elemento=df_auction.iloc[x, 2]
    if isinstance(elemento, str):
        if "(" in elemento:
            
            df_auction.loc[x] = pd.NA
        
        

df_auction.dropna(inplace=True)



#give a unique number for each zone
df_auction["Zone_num"] = df_auction["Zone"].map({
"corvetto-rogoredo": 1, 
"precotto-turro": 2, 
"pasteur-rovereto": 3,
"ripamonti-vigentino": 4, 
"citta-studi-susa": 5, 
"solari-washington": 6,
"san-siro-trenno": 7, 
"porta-romana-cadore-montenero": 8, 
"porta-venezia-indipendenza": 9,
"fiera-sempione-city-life-portello": 10,
"zona-navigli": 11, 
"garibaldi-moscova-porta-nuova": 12, 
"quadronno-palestro-guastalla": 13,
"genova-ticinese": 14, 
"arco-della-pace-arena-pagano": 15, 
"centrale-repubblica": 16,
"bicocca-niguarda": 17, 
"cenisio-sarpi-isola": 18, 
"affori-bovisa": 19,
"viale-certosa-cascina-merlata": 20,
"bisceglie-baggio-olmi": 21, 
"bande-nere-inganni": 22, 
"forlanini": 23,
"famagosta-barona": 24, 
"maggiolina-istria": 25, 
"abbiategrasso-chiesa-rossa": 26,
"udine-lambrate": 27, 
"porta-vittoria-lodi": 28, 
"ponte-lambro-santa-giulia": 29,
"cimiano-crescenzago-adriano": 30,
"napoli-soderini": 31, 
"centro": 32 

})





df_auction.to_csv('houses_auction.csv', index=False)





df_auction = pd.read_csv('houses_auction.csv')
#adding a row when the zone is missing

i=1
s=len(df_auction['Zone'])
while i < s:
    print(i)
    if df_auction.iloc[i+1]['Zone_num'] > df_auction.iloc[i]['Zone_num']+1:
        new_row = pd.DataFrame({'Name': 'CAMPO VUOTO', 'Zone': 'CAMPO VUOTO','Price': 0, 'Surface': 0,'Zone_num': df_auction.iloc[i]['Zone_num']+1}, index=[i+1])
        df_auction = pd.concat([df_auction.iloc[:i+1], new_row, df_auction.iloc[i+1:]]).reset_index(drop=True)
        #i=1
    i=i+1
df_auction.to_csv('houses_auction.csv', index=False)