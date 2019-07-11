# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 08:40:07 2019

@author: khushal
"""
import pandas as pd
## Numpy to pandas
import numpy as np
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
print(input_data_df.dtypes)
print("head = ",input_data_df.head())
print("tail = ",input_data_df.tail())
print("describe = ",input_data_df.describe())
print(input_data_df.shape)
print(len(input_data_df))
print(type(input_data_df))
#To select multiple columns, you need to use two times the bracket, [[..,..]]
print(input_data_df['EFFBMY'])
### using a slice for row
print(input_data_df[0:3])


## Concatenation
import numpy as np
import pandas as pd
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
print(len(df_concat))
print(df_concat.sort_values('Age'))
print(df_concat.drop_duplicates('name'))

###
import pandas as pd
path = "file:///C:/Users/khushal/Documents/Python Scripts/StateUT-wise educational status of suicide victim during 2001-2012.xls"

df_xlx= pd.read_excel(path)
print("Get unique values from df = ", df_xlx['STATE/UT'].unique())
print(" Transpose = ",df_xlx.T)

#############################

import pandas as pd
start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)

print(pd.date_range(start, end))


import pandas as pd

#By passing a string literal, we can create a timedelta object.
print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))

#By passing an integer value with the unit, an argument creates a Timedelta object.
print(pd.Timedelta(6,unit='h'))

#Data offsets such as - weeks, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds can also be used in construction.
print(pd.Timedelta(days=2))

#Example #1: Using isnull()

# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("file:///C:/Users/khushal/Documents/Python Scripts/employees.csv") 

print(data.isnull())
# creating bool series True for NaN values 
bool_series = pd.notnull(data["Gender"]) 

# filtering data 
# displayind data only with team = NaN 
data[bool_series] 

#Example #1: Using notnull()

print(data.notnull())
# creating bool series False for NaN values 
bool_series = pd.notnull(data["Gender"]) 
  
# displayed data only with team = NaN 
data[bool_series] 


# create a empty dataframe
import pandas as pd
df = pd.DataFrame(columns=['A'])
print("dataframe = ",df)

# Dealing with NaN values.
import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, 5],
                    [np.nan, 3, np.nan, 4]],
                    columns=list('ABCD'))

print("dataframe before Nan = ",df)
df.fillna(0)
print("dataframe after = ",df)


df1 = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                             pd.NaT]})
# removing null values to avoid errors   
#axis : {0 or ‘index’, 1 or 'columns'}, default 0
#inplace : bool, default False = If True, do operation inplace and return None.
df2 = df1.dropna(axis='columns')
print("Dropping Nan values = ",df2) 


### Reading a json file
import pandas as pd
path = "C:/Users/khushal/Documents/Python Scripts/Baji Yakkati Project/sample.json"
Line_df=pd.read_json(path, orient='values')
print(Line_df.dtypes)
print(" before coversion = ",Line_df.dtypes)
# method one
Line_df['odate'] =  pd.to_datetime(Line_df['odate']) # convert a column into datetime format

# method two
Line_df['odate'] = Line_df['odate'].astype('datetime64[ns]')  # convert a column into datetime format
print(" After coversion = ",Line_df.dtypes)
print("Line_df.info = ",Line_df.info)
Line_df['odate_1'] = Line_df['odate'].dt.strftime('%m/%d/%Y')
Line_df['odate_2'] = Line_df['odate'].dt.strftime('%B-%Y')
print(Line_df['odate'],Line_df['odate_1'],Line_df['odate_2'])

import pandas as pd 
# Creating Dataframe 
df = pd.DataFrame([['a', 'b'], ['c', 'd']], 
				index =['row 1', 'row 2'], 
				columns =['col 1', 'col 2']) 

# Indication of expected JSON string format 
print(df.to_json(orient ='split')) 
print(df.to_csv())
print(df.to_dict())
print(df.to_json(orient ='index')) 


##