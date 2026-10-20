import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load data
data = pd.read_csv("data/diabetes.csv")

# Split into features (X) and target (y)
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))

# Save the trained model
joblib.dump(model, "model/diabetes_model.pkl")
print("\nModel saved successfully!")
