# Import necessary libraries for machine learning and data processing
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.linear_model import LinearRegression    # Linear regression model
from sklearn.metrics import mean_squared_error, r2_score  # For evaluating model performance
import matplotlib.pyplot as plt                      # For visualizing results
from sklearn.preprocessing import StandardScaler     # For feature scaling (standardization)
from sklearn.model_selection import cross_val_score  # For cross-validation to evaluate model performance

# Importing custom module for querying data (assumes a specific data pipeline in './sources/queries/')
import sys
sys.path.append('./sources/queries/')
from query_genre_rating import query_genre_rating    # Function to fetch the dataset

# Fetch the dataset using the custom query function
df = query_genre_rating()

# Select features and target variables for the regression model
# X contains the independent variables: 'movies' and 'users'
X = df[['movies', 'users']]

# Standardize the features to have mean = 0 and standard deviation = 1
# Standardization helps improve the performance of machine learning models by normalizing feature scales
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# y contains the target variable: 'rating', which we aim to predict
y = df['rating']

# Split the data into training and testing sets
# 80% of the data is used for training, 20% for testing
# random_state ensures reproducibility of the split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Use the trained model to make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance using two metrics:
# Mean Squared Error (MSE): Measures the average squared difference between actual and predicted values
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))

# R-squared (R2): Measures how well the model explains the variance in the target variable
# R2 ranges from 0 (no explanatory power) to 1 (perfect explanation)
print("R-squared Score (R2):", r2_score(y_test, y_pred))

# Perform cross-validation to evaluate the model's performance more robustly
# Splits the data into 5 folds, trains the model on each fold, and computes R2 scores
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
print("Cross-validated R-squared Scores:", cv_scores)  # R2 scores for each fold
print("Average R-squared Score:", cv_scores.mean())    # Mean R2 score across all folds

# Visualize the relationship between predicted values and actual values
# This helps assess how well the model's predictions align with the ground truth
plt.figure(figsize=(10, 6))  # Set the size of the plot
plt.scatter(y_test, y_pred, alpha=0.7)  # Scatter plot of actual vs. predicted values
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
# The red dashed line represents a perfect prediction (y = x)
plt.title("Predictions vs. Actual Values")  # Title of the plot
plt.xlabel("Actual Values")  # X-axis label
plt.ylabel("Predictions")    # Y-axis label
plt.show()  # Display the plot