import sys
sys.path.append('./sources/queries/')
from query_movies_rating import query_movies_rating
import seaborn as sns
import matplotlib.pyplot as plt

df = query_movies_rating()

# Bar Chart: Average rating by genre

plt.figure(figsize=(14, 6))
barplot = sns.barplot(data=df, x='genre', y='rating', palette='viridis', ci=None)
# Add the labels
for p in barplot.patches:
    barplot.annotate(
        format(p.get_height(), '.2f'),
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center', xytext=(0, 12), textcoords='offset points'
    )

plt.xticks(rotation=30, ha='right')  # Adjust rotation and alignment
plt.title("Average Rating by Genre")
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