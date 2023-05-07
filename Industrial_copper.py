
import pandas as pd
from datetime import datetime
import numpy as np


data = pd.read_excel(r"G:/GUVI_ZEN_PY/copper_data.xlsx")

df=data.copy()

df.columns #list of columns



df.drop(columns=['ID'],inplace=True)


df.describe()


df.dtypes #checking data types



df.isnull().sum() #looking for null values


df.nunique() #unique values in columns


df.head()


a=df['Material_Reference'].str.startswith("000000")
print(a)
b=(a==True)
df['Material_Reference'][b] = np.NaN


#Categorical Variable
cat_var = ['Status','Item_Type','Material_Reference','Product_Reference']

#Continuous Variables
cont_var = ['Quantity_Tons','Customer','Delivery_Country','Application','Thickness','Width','Selling_Price']


#columns with null values
col_n = [df.columns[df.isnull().sum()>0]]
col_n





