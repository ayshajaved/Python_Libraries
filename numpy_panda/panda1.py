import pandas as pd
import numpy as nm

#we can create series in panda using numpy random function
# series = pd.Series(nm.random.random(10))
# print(series, series.dtype, series.shape)

# data = {
 # "name" : "ayesha",
# "age"  : 20,
# "qualification" : "Fsc pre-medical",
# "university": "CUI"
# }

# d = pd.Series(data);print(d)

#dataframes using numpy
#random and randint can't be used, randint takes high, low and size parameters
# df = pd.DataFrame(nm.random.rand(5, 3))  #5 rows and 3 columns
# print(df) 
# df.index = nm.arange(1,6)     #row index is changed
# print(df) 
# df.columns = ["a","b", "c"]   #col index is changed
# print(df)
# print(df.columns, df.index)

#another way of index
# df = pd.DataFrame(nm.random.rand(5, 3), index= nm.arange(1,6), columns=["a", "b", "c"])  #5 rows and 3 columns
# print(df) 
# print(df.columns, df.index)

# Data = {
#     "names" : ("ayesha", "fatima", "amna", "tehreem"),
#     "marks" : (100, 98,87, 97)
# }
# d = pd.DataFrame(Data)
# print(d)
# d.to_csv("Pan.csv") #pass index as false to eliminate index from csv file
# '''
# head and tails in Dataframes
# '''
# print(d.head(2))         #returns the number of first rows given as parameter
# print(d.tail(2))         #returns the number of last rows given as parameter

#customindexing 
# colleges = {
#     "names" : ["comsats", "university of lahore", "university of central punjab"],
#     "fee"   : ["High", "moderte", "low"]
#     }
# d = pd.DataFrame(colleges)
# print(d)
# #we can change the index of the colleges according to their alias
# d.index= ["cui", "uol", "ucp"]; print(d)
# d.to_csv("colleges.csv")

# #describe function describes only the numeric data
# print(d.describe())    

