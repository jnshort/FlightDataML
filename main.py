import pandas as pd 
import sys
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

    # Validate the altitude
    try:
        alt = sys.argv[1]
        alt = float(alt)
        if alt < 0:
            print("Altitude must be positive")
            sys.exit(1)
        if alt > 50000:
            print("Insuffient training data\nAltitude must be less than 50,000 ft")
            sys.exit(1)
    except IndexError:
        print("Please provide an altitude")
        sys.exit(1)
    except ValueError:
        print("Altitude must be a number")
        sys.exit(1)

    alt_poly = poly.transform([[alt]])
    alt_scaled = scaler.transform(alt_poly)
    mph = model.predict(alt_scaled)
    print(f"Predicted speed at {alt} ft: {mph[0][0]:.2f} mph")