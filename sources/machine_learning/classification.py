from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import sys
sys.path.append('./sources/queries/')
from query_genre_rating import query_genre_rating

df = query_genre_rating()

# Create a binary variable: High ratings (>4) or Low ratings (≤4)
df['high_rating'] = (df['rating'] > 4).astype(int)

# Select features
X = df[['movies', 'users']]
y = df['high_rating']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Model
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = tree.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Visualizing the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(tree, feature_names=['movies', 'users'], class_names=['Low', 'High'], filled=True)
plt.title("Decision Tree for High Rating Prediction")
plt.show()
