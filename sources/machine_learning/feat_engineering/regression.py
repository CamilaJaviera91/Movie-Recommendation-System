from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Add the directory containing query_genre_rating to system path
# This allows us to import the function 'positive_vs_negative_reviews' from a custom location
sys.path.append('./sources/queries/feat_engineering/')
from positive_vs_negative_reviews import positive_vs_negative_reviews

# Load dataset using the query function
# The function 'positive_vs_negative_reviews' retrieves the review data
df = positive_vs_negative_reviews()

# Check if the dataset is loaded correctly by displaying the first few rows
# This is useful for inspecting the structure and contents of the dataset
print(df.head())

# One-hot encode the 'genre' categorical feature
# 'get_dummies()' is used to convert the 'genre' column into multiple binary columns, 
# one for each unique genre, and 'drop_first=True' avoids multicollinearity by 
# removing the first category (the reference category)
df = pd.get_dummies(df, columns=['genre'], drop_first=True)

# Define features (X) and target variable (y)
# X consists of all columns except 'movies' and 'total_reviews' (these are not useful as features for prediction)
# y is the target column, which we want to predict, in this case 'total_reviews'
X = df.drop(columns=['movies', 'total_reviews'])
y = df['total_reviews']

# Split the dataset into training and testing sets
# 80% of the data will be used for training, and 20% will be reserved for testing
# The 'random_state' ensures reproducibility by fixing the random splitting seed
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
# LinearRegression is suitable for predicting continuous values like 'total_reviews'
model = LinearRegression()

# Train the model using the training data
# The model learns the relationship between the features (X_train) and the target (y_train)
model.fit(X_train, y_train)

# Use the trained model to make predictions on the test data
# The model predicts the target variable ('total_reviews') for the unseen test data (X_test)
y_pred = model.predict(X_test)

# Evaluate the model's performance using Mean Squared Error (MSE)
# MSE is a common metric for regression tasks; it measures the average squared difference 
# between predicted and actual values, with lower values indicating better performance
print("MSE:", mean_squared_error(y_test, y_pred))

# Evaluate the model using the R² score
# The R² score represents the proportion of variance explained by the model; 
# a higher R² score means the model is better at explaining the target variable
print("R² Score:", r2_score(y_test, y_pred))

# Optional: Visualize the actual vs predicted values
# A scatter plot helps to visually inspect how well the predictions match the true values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')  # X-axis represents the actual values of the target variable
plt.ylabel('Predicted Values')  # Y-axis represents the predicted values
plt.title('Actual vs Predicted')  # Title for the plot
plt.show()  # Display the plot