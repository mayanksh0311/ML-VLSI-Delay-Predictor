import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib  # To save the model for later use

# 1. Load the dataset
df = pd.read_csv('circuit_data.csv')

# 2. Separate Features (X) and Target (y)
# Features: The hardware specs (Bit Width, Gate Count)
X = df[['Bit_Width', 'Gate_Count']]
# Target: The result we want to predict (Delay)
y = df['Delay_ns']

# 3. Split into Training and Testing sets
# We hide 20% of data (Test set) to see if the model can predict circuits it hasn't seen before.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Model
model = LinearRegression()
print("Training model on 80% of the circuits...")
model.fit(X_train, y_train)

# 5. Evaluate the Model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("------------------------------------------------")
print(f"Model Performance:")
print(f"Average Error (MAE): {mae:.4f} ns")
print(f"Accuracy Score (R2): {r2:.4f} (1.0 is perfect)")
print("------------------------------------------------")

# 6. Save the trained model to a file
joblib.dump(model, 'delay_predictor_model.pkl')
print("Model saved as 'delay_predictor_model.pkl'")