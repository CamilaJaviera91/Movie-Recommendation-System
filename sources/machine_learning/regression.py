from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score


import sys
sys.path.append('./sources/queries/')
from query_genre_rating import query_genre_rating

df = query_genre_rating()

# Select features

X = df[['movies', 'users']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
y = df['rating']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R-squared Score (R2):", r2_score(y_test, y_pred))

cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
print("Cross-validated R-squared Scores:", cv_scores)
print("Average R-squared Score:", cv_scores.mean())


# Visualizing Predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title("Predictions vs. Actual Values")
plt.xlabel("Actual Values")
plt.ylabel("Predictions")
plt.show()