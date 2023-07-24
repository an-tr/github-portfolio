import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import category_encoders as ce
import seaborn as sns
import matplotlib.pyplot as plt


#opening files
data = pd.read_csv("houses_rent.csv")
data_p=data

#functions

#return the percentage of the correct values within a margin 
def accuracy(predictions, labels, margin):
    correct = 0
    for i in range(len(predictions)):
        
        if abs(predictions[i] - labels[i]) <= margin:
            correct += 1
            
    return correct / len(predictions)

#returns the margin where the best elements are
    
    for i in range(5000):
        
        if accuracy(predictions, labels, i)>=limit:
            return i

#print the best values within the specific margin  
def print_precisione(predictions, labels):
    print('20% migliori: ',valuebox(predictions, labels,0.2))
    print('40% migliori: ',valuebox(predictions, labels,0.4))
    print('60% migliori: ',valuebox(predictions, labels,0.6))
    print('80% migliori: ',valuebox(predictions, labels,0.8))
    print('90% migliori: ',valuebox(predictions, labels,0.9))
    print('100% migliori: ',valuebox(predictions, labels,1))
    print('\n\n')

#print prediciton and the real value that have an error above a range value 
def printa_outliner(predictions, labels,margin):
    
    for i in range(len(predictions)):
       
        if abs(predictions[i] - labels[i]) >= margin:
            print('EFFETTIVO: ',labels[i],'PREDETTO: ',predictions[i])
            
    

#trasform zone data

ce_OHE = ce.OneHotEncoder(cols=['Zone_num'])
data = ce_OHE.fit_transform(data)


#splitting data
xx = np.array(data[["Surface","Zone_num_1","Zone_num_2","Zone_num_3","Zone_num_4","Zone_num_5","Zone_num_6","Zone_num_7","Zone_num_8","Zone_num_9","Zone_num_10","Zone_num_11","Zone_num_12","Zone_num_13","Zone_num_14","Zone_num_15","Zone_num_16","Zone_num_17","Zone_num_18","Zone_num_19","Zone_num_20","Zone_num_21","Zone_num_22","Zone_num_23","Zone_num_24","Zone_num_25","Zone_num_26","Zone_num_27","Zone_num_28","Zone_num_29","Zone_num_30","Zone_num_31","Zone_num_32"]])

yy = np.array(data[["Price"]])

xtrain, xtest, ytrain, ytest = train_test_split(xx, yy, 
                                                test_size=0.10, 
                                                random_state=42)



############################ linear regression
model_lineare=LinearRegression()
model_lineare.fit(xtrain, ytrain)
############################





#calculate the accuracy

print("REGRESSIONE LINEARE")
print_precisione(model_lineare.predict(xtest), ytest)


#creating a new table like the auction table with a new column of the predicition of the possible rent for each house that is in auction at the moment
df_asta = pd.read_csv('houses_auction.csv')


ce_OHE = ce.OneHotEncoder(cols=['Zone_num'])
df_asta_tr = ce_OHE.fit_transform(df_asta)

df_asta_tr = df_asta_tr.drop('Name', axis=1)
df_asta_tr = df_asta_tr.drop('Zone', axis=1)
df_asta_tr = df_asta_tr.drop('Price', axis=1)

#adding column

nuova_colonna=model_lineare.predict(df_asta_tr.values)
df_asta=df_asta.assign(Prediction=nuova_colonna)
df_asta['Prediction']=df_asta['Prediction'].round(0)

df_asta.to_csv('prediction.csv', index=False)

