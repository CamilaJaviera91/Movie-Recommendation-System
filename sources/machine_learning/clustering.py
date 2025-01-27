import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import sys
sys.path.append('./sources/queries/')
from query_genre_rating import query_genre_rating

df = query_genre_rating()

# Validate DataFrame and select features
required_columns = ['movies', 'users', 'rating']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"DataFrame is missing required columns: {required_columns}")

# Handle missing values
features = df[['movies', 'users', 'rating']].fillna(0)

# Normalize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K-Means Model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(features_scaled)

# Convert cluster to categorical for better visualization
df['cluster'] = df['cluster'].astype('category')

# Visualize the clusters
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=df, x='users', y='rating', hue='cluster', palette='viridis', s=100
)
plt.title("Genre Clustering Based on Users and Ratings")
plt.xlabel("Number of Users")
plt.ylabel("Average Rating")
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.show()
