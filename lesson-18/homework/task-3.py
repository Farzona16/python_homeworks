import pandas as pd
import numpy as np

#task-1
iris_df = pd.read_json("iris.json")
iris_stats = iris_df.describe().T  
iris_stats["median"] = iris_df.median(numeric_only=True)  
iris_results = iris_stats[["mean", "median", "std"]]  
print(iris_results)

# task-2
titanic_df = pd.read_excel("titanic.xlsx")
age_min = titanic_df["Age"].min()
age_max = titanic_df["Age"].max()
age_sum = titanic_df["Age"].sum()
titanic_results = {"min_age": age_min, "max_age": age_max, "sum_age": age_sum}
print(titanic_results)


#task-3
movie_df = pd.read_csv("movie.csv")

top_director = (
    movie_df.groupby("director_name")["director_facebook_likes"]
    .sum()
    .idxmax()
)

longest_movies = (
    movie_df.nlargest(5, "duration")[["movie_title", "director_name", "duration"]]
)

print("\nDirector with highest total Facebook likes:", top_director)
print("\nTop 5 longest movies:\n", longest_movies)
