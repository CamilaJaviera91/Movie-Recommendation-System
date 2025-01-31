import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import sys

# Add the directory containing query_genre_rating to system path
sys.path.append('./sources/queries/')
from query_genre_rating import query_genre_rating

# Load dataset using the query function
df = query_genre_rating()

# Validate DataFrame and ensure required columns exist
required_columns = ['movies', 'users', 'rating']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"DataFrame is missing required columns: {required_columns}")

# Handle missing values by replacing them with 0
features = df[['movies', 'users', 'rating']].fillna(0)

# Normalize the features using StandardScaler to standardize values
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Initialize K-Means clustering model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Fit the model and predict clusters
df['cluster'] = kmeans.fit_predict(features_scaled)

# Convert cluster labels to categorical for better visualization
df['cluster'] = df['cluster'].astype('category')

# Visualize the clusters using a scatter plot
plt.figure(figsize=(10, 6))  # Set figure size
scatter = sns.scatterplot(
    data=df, x='users', y='rating', hue='cluster', palette='viridis', s=100
)
plt.title("Genre Clustering Based on Users and Ratings")  # Add plot title
plt.xlabel("Number of Users")  # Label x-axis
plt.ylabel("Average Rating")  # Label y-axis
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.show()