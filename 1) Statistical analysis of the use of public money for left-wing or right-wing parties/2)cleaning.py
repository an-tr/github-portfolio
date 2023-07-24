import pandas as pd

df_pol = pd.read_csv('politcs_raw.csv')

#cleaning data
         
df_pol.dropna(inplace=True)



df_pol["tot_invest"] = df_pol['tot_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["amministration_invest"] = df_pol['amministration_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["social_invest"] = df_pol['social_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["environment_invest"] = df_pol['environment_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["transport_invest"] = df_pol['transport_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["education_invest"] = df_pol['education_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["culture_invest"] = df_pol['culture_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["sport_invest"] = df_pol['sport_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["tourism_invest"] = df_pol['tourism_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["economic_invest"] = df_pol['economic_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["sevice_invest"] = df_pol['sevice_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["police_invest"] = df_pol['police_invest'].replace('INVESTIMENTI ', '', regex=True)
df_pol["justice_invest"] = df_pol['justice_invest'].replace('INVESTIMENTI ', '', regex=True)

selected_columns = df_pol.columns[3:16]

for c in range(len(df_pol.columns)):
    for r in range(len(df_pol.index)):
        
        if isinstance(df_pol.iloc[r, c], str):
            if 'milioni' in df_pol.iloc[r, c]:
                df_pol.iloc[r, c]=df_pol.iloc[r, c].replace('milioni','').replace(' ','').replace(',','.')
                df_pol.iloc[r, c]=1000000*float(df_pol.iloc[r, c])
        if isinstance(df_pol.iloc[r, c], str):    
            if 'milione' in df_pol.iloc[r, c]:
                df_pol.iloc[r, c]=df_pol.iloc[r, c].replace('milione','').replace(' ','').replace(',','.')
                df_pol.iloc[r, c]=1000000*float(df_pol.iloc[r, c])

        if isinstance(df_pol.iloc[r, c], str):
            if 'miliardi' in df_pol.iloc[r, c]:
                df_pol.iloc[r, c]=df_pol.iloc[r, c].replace('miliardi','').replace(' ','').replace(',','.')
                df_pol.iloc[r, c]=1000000000*float(df_pol.iloc[r, c])
            




# give each party the right or left label

df_pol["orientation"] = df_pol["party"].map({

"PDL": "Right", 
"PD": "Left", 
"FI": "Right",
"DS":"Left",
"DL":"Left",
"MSI-DN":"Right",
"IDV":"Left",
"NCD":"Right",
"AN":"Right",
"SEL":"Left",
"ULIVO":"Left",
"FRATELLI D'ITALIA CENTRODESTRA NAZIONALE":"Right",
"LEGA":"Right",
"SINISTRA ARCOBALENO":"Left",
"M5S":"Left",
"CEN-DES":"Right",
"CEN-SIN(LS.CIVICHE)":"Left",
"LISTA CIVICA - CEN-SIN":"Left",


})
#transform the data of each category of investment as a percentage of the total investment in that year 
df_pol= df_pol.dropna(subset=['orientation'])


for c in range(len(df_pol.columns)):
    for r in range(len(df_pol.index)):
        try:
            df_pol.iloc[r, c]=float(df_pol.iloc[r, c])
        except:
            pass   
        
            
        if (isinstance(df_pol.iloc[r, c], float) or isinstance(df_pol.iloc[r, c], int)) and c != 3:
            
            
            df_pol.iloc[r,c]=round((df_pol.iloc[r, c]*100)/(df_pol.iloc[r, 3]),2)





df_pol=df_pol.drop(['city', 'party', 'tot_invest'], axis=1)

#save as csv
df_pol.to_csv('politics.csv', index=False)

