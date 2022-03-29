from os import replace
import numpy as np
import pandas as pd

# Importing Data
dataM = "C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/athlete_medals_M.csv"
dataF = "C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/athlete_medals_F.csv"

dfM = pd.read_csv(dataM)
dfF = pd.read_csv(dataF)

# print(dfM.head(3))

# Replacing Medal values with 1
rep = ["Gold", "Silver", "Bronze"]
val = [1, 1, 1]

dfM['Medal'] = dfM['Medal'].replace(to_replace=rep, value=val)
dfF['Medal'] = dfF['Medal'].replace(to_replace=rep, value=val)

# print(dfF.head(6))

# Filling NaN values with mean 

dfM = dfM.fillna(dfM.mean())
dfF = dfF.fillna(dfF.mean())
# print(dfF.head(6))

# Saving new csv files 
# dfM.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/athlete_medals_M1.csv")
# dfF.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/athlete_medals_F1.csv")

dfM_age = dfM['Age'].value_counts(bins = [1,10,20,30,40,50,60,70]).to_frame()
dfF_age = dfF['Age'].value_counts(bins = [1,10,20,30,40,50,60,70]).to_frame()
dfM_h = dfM['Height'].value_counts(bins = [140,150,160,170,180,190,200,210,220,230]).to_frame()
dfF_h = dfF['Height'].value_counts(bins = [140,150,160,170,180,190,200,210,220,230]).to_frame()
dfM_w = dfM['Weight'].value_counts(bins = [30,50,70,90,110,130,150,170,190]).to_frame()
dfF_w = dfF['Weight'].value_counts(bins = [30,50,70,90,110,130,150,170,190]).to_frame()

dfM_age.index.name = 'Age'
dfF_age.index.name = 'Age'
dfM_h.index.name = 'Height'
dfM_h.index.name = 'Height'
dfM_w.index.name = 'Weight'
dfF_w.index.name = 'Weight'

dfM_age.rename(columns = {'Age':'Medal_Count'}, 
            inplace = True)
dfF_age.rename(columns = {'Age':'Medal_Count'}, 
            inplace = True)
dfM_h.rename(columns = {'Height':'Medal_Count'}, 
            inplace = True)
dfF_h.rename(columns = {'Height':'Medal_Count'}, 
            inplace = True)
dfM_w.rename(columns = {'Weight':'Medal_Count'}, 
            inplace = True)
dfF_w.rename(columns = {'Weight':'Medal_Count'}, 
            inplace = True)
# print(dfM_age)


dfM_age.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/M_age.csv")
dfF_age.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/F_age.csv")
dfM_h.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/M_h.csv")
dfF_h.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/F_h.csv")
dfM_w.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/M_w.csv")
dfF_w.to_csv("C:/Users/rohan/Desktop/UMassD_studies/Sem_2/Data_Viz/M_Proj/Datasets/Olympic_Athletes/F_w.csv")

