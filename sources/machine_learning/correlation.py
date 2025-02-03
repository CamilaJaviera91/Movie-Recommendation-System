import seaborn as sns
import matplotlib.pyplot as plt  # For visualizing results

# Importing custom module for querying data (assumes a specific data pipeline in './sources/queries/')
import sys
sys.path.append('./sources/queries/')  # Adding the custom module path to system path
from query_genre_rating import query_genre_rating  # Importing function to fetch the dataset

# Fetch the dataset using the custom query function
df = query_genre_rating()  # Assumes this function returns a Pandas DataFrame

if df is None:
    raise ValueError("query_genre_rating() returned None. Check your function implementation.")

# Compute the correlation matrix of the dataset
corr_matrix = df.select_dtypes(include=['number']).corr()  # Calculates Pearson correlation coefficients between numerical features

# Create a heatmap to visualize feature correlations
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")  
plt.title("Feature Correlation Heatmap")  # Add title to the plot
plt.show()  # Display the plot