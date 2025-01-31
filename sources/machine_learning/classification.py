from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import sys

# Add the directory containing query_genre_rating to system path
sys.path.append('./sources/queries/')
from query_genre_rating import query_genre_rating

# Load dataset using the query function
df = query_genre_rating()

# Create a binary target variable: 1 if rating > 4 (High), otherwise 0 (Low)
df['high_rating'] = (df['rating'] > 4).astype(int)

# Select feature columns (movies and users) and target variable
X = df[['movies', 'users']]  # Features
y = df['high_rating']  # Target variable

# Split the dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Decision Tree model with a maximum depth of 3
tree = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train the Decision Tree model on the training data
tree.fit(X_train, y_train)

# Make predictions on the test dataset
y_pred = tree.predict(X_test)

# Evaluate model performance
print("Model Accuracy:", accuracy_score(y_test, y_pred))  # Print accuracy score
print("Classification Report:\n", classification_report(y_test, y_pred))  # Print detailed classification metrics

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))  # Set figure size
plot_tree(tree, feature_names=['movies', 'users'], class_names=['Low', 'High'], filled=True)
plt.title("Decision Tree for High Rating Prediction")  # Add title to the plot
plt.show()