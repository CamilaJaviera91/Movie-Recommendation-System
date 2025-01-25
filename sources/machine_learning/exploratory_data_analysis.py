import sys
sys.path.append('./sources/queries/')
from query_movies_rating import query_movies_rating
import seaborn as sns
import matplotlib.pyplot as plt

df = query_movies_rating()

# Bar Chart: Average rating by genre

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='genre', y='rating', palette='viridis')
plt.xticks(rotation=50)
plt.title("Avegare Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.show()

# Scatter plot: Users vs Average Rating

plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='users', y='rating', hue='genre', palette='tab10', s=100)
plt.title("Relationship Bwetween Users and Average Ratings")
plt.xlabel("Number of Users")
plt.ylabel("Average Rating")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()