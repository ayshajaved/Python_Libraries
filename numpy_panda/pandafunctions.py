'''
here we will convert the panda dataframe to a 2d array
'''
import pandas as pd
import numpy as nm
# df = pd.DataFrame(nm.random.rand(5, 4))
# print(df)
# print(df.to_numpy()) #2d array craeted

'''
converting the numpy array into a dataframe
'''
# arr = nm.empty((3,4),dtype = nm.int16)
# # print(arr)
# result = pd.DataFrame((arr), index = nm.arange(1,4), columns = nm.arange(1,5))
# print(result)

#sorting
'''
axis is 0 if to sort according to row index and 1 if to sort according to column index
ascending true if ascending and false if descending and inplace true then it modifies the original and false
then it creates new one
'''
# df = pd.DataFrame(nm.random.rand(5, 4))
# print(df) #same 
# print(df.sort_index(axis=0, ascending=False, inplace=False)) #modified 
# print(df) #same 
'''
drop
'''
df = pd.DataFrame(nm.random.rand(3,3))
# print(df)
# print(df.drop(0, axis = 0))     #0 means horizontal
# print(df.drop(0, axis = 1))     #1 means vertical
#changes are not done to the original
'''
describe(), info(), mean(), count()
'''
print(df.describe())
print("------------------")
print(df.info())
print("------------------")
print(df.mean())
print("------------------")
print(df.count())
print("------------------")
print(df.all())

'''
concat function of pandas takes a dataframe or series and axis and returns a dataframe from two series
'''
# s1 = pd.Series([23, 45, 67, 45])
# # print(s1)
# s2 = pd.Series(["ayesha","fatima", "amna", "tehreem"])
# # print(s2)
# #making dict
# dic = {
#     "id" : s2,
#     "marks" : s1
# }

# print(pd.concat(dic, axis = 1)) #join argumnet can also be passed
'''
Outer Join: You use join='outer' when you want to see all data, even if some of it is missing.
Inner Join: You use join='inner' when you only want to see complete data (i.e., only those who have grades in both subjects).
'''

'''
merge function 
The merge function is used to combine two DataFrame objects based on one or more common keys (like SQL joins).
'''
# df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
# df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value2': [4, 5, 6]})
# result = pd.merge(df1, df2, on='key', how='inner')
# print(result)
 
# s1 = pd.Series([23, 45, 67, 45], name="marks")
# s2 = pd.Series(["ayesha","fatima", "amna", "tehreem"], name = "names")
# result = pd.merge(s1, s2, how = "outer", right_index=True, left_index= True )
# print(result)