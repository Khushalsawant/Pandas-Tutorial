# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 08:40:07 2019

@author: khushal
"""
import pandas as pd
## Numpy to pandas
import numpy as np
import random
h = [[1,2],[3,4]] 
df_h = pd.DataFrame(h)
print('Data Frame:', df_h)

## Pandas to numpy
df_h_n = np.array(df_h)
print('Numpy array:', df_h_n)

# a dictionary to create a Pandas dataframe.
dic = {'Name': ["John", "Smith"], 'Age': [30, 40]}
df_dic = pd.DataFrame(data=dic)	
print('Data Frame:', df_dic)			

#frequency: day: 'D,' month: 'M' and year: 'Y.'
## Create date
# Days
dates_d = pd.date_range('20300101', periods=6, freq='D')
print('Day:', dates_d)
# Months
dates_m = pd.date_range('20300101', periods=6, freq='M')
print('Month:', dates_m)

#describe(). It provides the counts, mean, std, min, max and percentile of the dataset.
path_of_input_file = "file:///C:/Users/khushal/Documents/Python Scripts/YTD_KPO_IT_Attrition.csv "
input_data_df = pd.read_csv(path_of_input_file)
print(input_data_df.columns)
print(input_data_df.index)
print("head = ",input_data_df.head(3))
print("tail = ",input_data_df.tail(3))
print("describe = ",input_data_df.describe())

#To select multiple columns, you need to use two times the bracket, [[..,..]]
print(input_data_df['EFFBMY'])
### using a slice for row
print(input_data_df[0:2])


## Concatenation
import numpy as np
df1 = pd.DataFrame({'name': ['John', 'Smith','Paul'],
                     'Age': ['25', '30', '50']},
                    index=[0, 1, 2])
df2 = pd.DataFrame({'name': ['Adam', 'Smith' ],
                     'Age': ['26', '11']},
                    index=[3, 4])  

df_concat = pd.concat([df1,df2]) 
print("df_concat = ",df_concat)
df_merge = pd.merge(df1,df2,on=['name'])
print("df_merge = ",df_merge)
