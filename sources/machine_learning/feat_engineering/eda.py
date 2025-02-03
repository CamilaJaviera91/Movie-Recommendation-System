import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Add the directory containing query_genre_rating to system path
sys.path.append('./sources/queries/feat_engineering/')
from positive_vs_negative_reviews import positive_vs_negative_reviews

# Load dataset using the query function
df = positive_vs_negative_reviews()

# Check basic statistics
print(df.describe())

# Histogram of positive and negative reviews
df[['positive_reviews', 'negative_reviews']].hist(bins=20, figsize=(10, 5))
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()