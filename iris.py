import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
data = load_iris()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
# Check the features and target labels
print("Features (X):")
print(X)  # This will print the input data (sepal/petal dimensions)

print("Target Labels (y):")
print(y)  # This will print the species of the iris flowers (0, 1, or 2)
# Check the features and target labels
# Check the shape of training and test data
print("Training data shape (X_train):", X_train.shape)
print("Testing data shape (X_test):", X_test.shape)
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Check if the model has been trained
print("Model trained successfully.")
# Make predictions on the test data
y_pred = model.predict(X_test)

# Print predicted values
print("Predicted values:", y_pred)

# Print actual values for comparison
print("Actual values:", y_test)

