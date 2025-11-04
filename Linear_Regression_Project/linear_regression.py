# Linear Regression Example: Car Mileage Prediction (Large Dataset)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Load dataset
data = pd.read_csv("car_mileage.csv")

# Step 2: Define feature (X) and target (y)
X = data[['Engine_Size (cc)']]
y = data['Mileage (km/l)']

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict for a new engine size
engine_size = 2500
predicted_mileage = model.predict([[engine_size]])
print(f"Predicted mileage for {engine_size} cc engine = {predicted_mileage[0]:.2f} km/l")

# Step 5: Visualization
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Engine Size (cc)')
plt.ylabel('Mileage (km/l)')
plt.title('Car Mileage Prediction using Linear Regression')
plt.legend()
plt.show()
