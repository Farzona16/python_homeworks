import pandas as pd
import sqlite3

#Part-1

#task-1
try:
    connect=sqlite3.connect('chinook.db')
    query="SELECT*FROM Customers"
    df=pd.read_sql(query, connect)
    print(df.head(10))
    connect.close()
except Exception as e:
    print(f"Error occurred: {e}")

#task-2
try:
    df=pd.read_json("iris.json")
    print(df.shape)
    print(df.columns)
except Exception as e:
    print(f"Error occurred: {e}")

#task-3
try:
    df=pd.read_excel("titanic.xlsx")
    print(df.head(5))
except Exception as e:
    print(f"Error occurred: {e}")

#task-5
try:
    df=pd.read_csv('movie.csv')
    print(df.sample(10))
except Exception as e:
    print(f"Error occurred: {e}")