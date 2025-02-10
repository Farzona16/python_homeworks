import pandas as pd
import numpy as np


# matrix=np.random.randint(1,100,10)
# matrix_mean=matrix.mean()
# matrix_median=np.median(matrix)
# matrix_std=np.std(matrix)
# print(matrix)
# print(matrix_mean)
# print(matrix_median)
# print(matrix_std)

# def multiplication_table(n):
#     n=int(n)
#     list=[]
#     for i in range(n):
#         a=f"{n} x {i} = {n*i}"
#         list.append(a)  
#     return list 
# b=multiplication_table(7)
# print(b)

# class Date:
#     def __init__(self,months,day,year):
#         self.months=months
#         self.day=day
#         self.year=year
#         self.list=["January","February","March","April","May","June","July","August","September",
#                    "October","November","December"]
#     def abs(self):
#         print(f"{self.months}/{self.day}/{self.year}")
    
#     def abd(self):
#         print(f"{self.list[self.months-1]} {self.day}, {self.year}")
#     def abcd(self):
#         print(f"{self.day} {self.list[self.months-1]}  {self.year}")                
# Date1=Date(12,25,2018)
# Date1.abs()
# Date1.abd()
# Date1.abcd()    

df=pd.read_csv("TestMax.csv")
df.head()
df['max_value']=df[['Max1','Max2','Max3']].max(axis=1)
a=df[['Year', 'max_value']]


