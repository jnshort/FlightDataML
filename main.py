import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

if __name__ == "__main__":
    # Load the data
    data = pd.read_csv("data/processed_data.csv")    

    # Split the data into features and target
    X = data['alt'].values.reshape(-1, 1)
    y = data['mph'].values.reshape(-1, 1)

    # Create the polynomial features
    poly = PolynomialFeatures(degree=3)
    X_poly = poly.fit_transform(X)

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_poly)

    # Fit the model
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Get altitude input from user
    alt = int(input("Enter altitude in feet: "))

    # Validate user input
    try:
        alt = int(alt)
    except ValueError:
        print("Invalid altitude")
        exit()
    if alt < 0:
        print("Invalid altitude")
        exit()

    alt_poly = poly.transform([[alt]])
    alt_scaled = scaler.transform(alt_poly)
    mph = model.predict(alt_scaled)
    print(f"Predicted speed at {alt} ft: {mph[0][0]} mph")