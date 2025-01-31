import sys

# Add the directory containing query_movies_rating to system path
sys.path.append('./sources/queries/')
from query_movies_rating import query_movies_rating
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset using the query function
df = query_movies_rating()

# Bar Chart: Average rating by genre
plt.figure(figsize=(14, 6))  # Set figure size
barplot = sns.barplot(data=df, x='genre', y='rating', palette='viridis', ci=None)  # Create bar chart

# Add labels above each bar
for p in barplot.patches:
    barplot.annotate(
        format(p.get_height(), '.2f'),  # Format rating values to 2 decimal places
        (p.get_x() + p.get_width() / 2., p.get_height()),  # Position text in the center of the bar
        ha='center', va='center', xytext=(0, 12), textcoords='offset points'  # Adjust text position
    )

# Adjust x-axis labels for better readability
plt.xticks(rotation=30, ha='right')
plt.title("Average Rating by Genre")  # Add title to the plot
plt.xlabel("Genre")  # Label x-axis
plt.ylabel("Average Rating")  # Label y-axis
plt.show()

# Scatter plot: Users vs Average Rating
plt.figure(figsize=(10, 6))  # Set figure size
scatterplot = sns.scatterplot(data=df, x='users', y='rating', hue='genre', palette='tab10', s=100)  # Create scatter plot

# Add labels for each point to display the number of users
for i in range(len(df)):
    plt.text(
        x=df['users'][i],
        y=df['rating'][i],
        s=f"{int(df['users'][i])}",  # Convert number of users to integer for display
        fontsize=9,
        color='black',
        ha='center'  # Center align text over points
    )

plt.title("Relationship Between Users and Average Ratings")  # Add title
plt.xlabel("Number of Users")  # Label x-axis
plt.ylabel("Average Rating")  # Label y-axis
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.show()