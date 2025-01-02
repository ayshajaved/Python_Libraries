import pandas as pd
import numpy as nm

'''
copying in pandas data set is same as copying in list
'''
# d = pd.DataFrame(
# {
#     'id' : [1,2,3,4,5],
#     'names' : ["ayesha","fatima", "amna", "tehreem", 'abdullah' ]
# }
# )
# print(d)
# d1 = d
# print(d1)
# #if i change in one, the other will be changed automatically
# d1.loc[2,"id"] = 10
# print(d1)
# #we can give index of column
# d1.iloc[2,0] = 10
# print(d1)

#we simply use the basic method of [][] changing, when the indexes are given
d = pd.DataFrame(nm.random.rand(3,3))
print(d)
# d1 = d
# d1[0][2] = 100
# print(d1)
#but this leads to unexpected behaviuor, so best way is to use .iloc, .loc, .at methods
# d1.iloc[0,1] = 1
# print(d1)
# print(d)
#both changes, to avoid use copy
d1 = d.copy()
d1.iloc[0,1] = 1
print(d1)
print(d)       #the first one remains intact