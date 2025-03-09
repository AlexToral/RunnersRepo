import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

csv = "./csv/savefile.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv)

# Select columns for graphing
graphCols = ["Date", "Pace"]

# Convert 'Date' to pandas datetime (with inferred format)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Convert 'Date' to numeric (e.g., days since the first date)
df['Date_numeric'] = (df['Date'] - df['Date'].min())  / pd.Timedelta(days=1)

# Prepare the data for linear regression
X = df['Date_numeric'].values.reshape(-1, 1)  # Features (dates)
y = df['Pace'].values  # Target (pace)

# Apply linear regression
model = LinearRegression()
model.fit(X, y)

# Make predictions using the linear regression model
y_pred = model.predict(X)

# Plotting
plt.scatter(df['Date'], df['Pace'], color='blue', label='Data Points')  # Scatter plot
plt.plot(df['Date'], y_pred, color='red', label='Prediction Line')  # Regression line

plt.title("Pace Through the Days")
plt.xlabel("Date")
plt.ylabel("Pace")
plt.legend()

plt.show()
