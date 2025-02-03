import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Add the directory containing query_genre_rating to system path
# This allows us to import the function from a custom location
sys.path.append('./sources/queries/feat_engineering/')
from positive_vs_negative_reviews import positive_vs_negative_reviews

# Load dataset using the query function
# The function 'positive_vs_negative_reviews' retrieves the review data
df = positive_vs_negative_reviews()

# Check basic statistics
# The describe() method provides summary statistics like mean, std, min, and max
print(df.describe())

# Histogram of positive and negative reviews
# Plotting the distribution of 'positive_reviews' and 'negative_reviews' with 20 bins
# This helps visualize the frequency distribution of both types of reviews
df[['positive_reviews', 'negative_reviews']].hist(bins=20, figsize=(10, 5))
plt.show()

# Correlation heatmap
# Using seaborn to plot the correlation matrix for numerical columns in the dataframe
# The 'coolwarm' color map shows the strength and direction of correlations
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()