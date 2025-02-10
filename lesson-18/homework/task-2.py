import pandas as pd

#task-1
try:
    df=pd.read_json("iris.json")
    df.columns=df.columns.str.lower()
    df_selected=df[['sepallength','sepalwidth']]
    print(df_selected.head())
except Exception as e:
    print(f"Error occurred: {e}")

# task-2
try:
    df=pd.read_excel('titanic.xlsx')
    df_filtered=[df[df["Age"]>30]]
    df_counter=df['Sex'].value_counts()
    print(df_filtered)
    print(df_counter)
except Exception as e:
    print(f"Error occurred: {e}")

#task-4
try:
    df=pd.read_csv("movie.csv")
    df_filtered=df[df["duration"]>120]
    df_sorted=df_filtered.sort_values(by='director_facebook_likes',ascending=False)
    print(df_filtered)
    print(df_sorted)
except Exception as e:
    print(f"Error occurred: {e}")