import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class Table():
    def __init__(self):
        self.csv = "./csv/savefile.csv"
        self.df = pd.read_csv(self.csv)
    
    def graphDateandPace(self):
        # Convertir 'Date' a tipo datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        # Eliminar filas con valores NaN en 'Date' o 'Pace'
        self.df = self.df.dropna(subset=['Date', 'Pace'])

        # Convertir fechas a valores numéricos
        self.df['Date_numeric'] = (self.df['Date'] - self.df['Date'].min()) / pd.Timedelta(days=1)

        # Definir variables de regresión
        X = self.df['Date_numeric'].values.reshape(-1, 1)  # Features (dates)
        y = self.df['Pace'].values  # Target (pace)

        # Ajustar modelo de regresión lineal
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        # Graficar
        plt.figure(figsize=(10, 5))
        plt.scatter(self.df['Date'], self.df['Pace'], color='blue', label='Data Points')  # Scatter plot
        plt.plot(self.df['Date'], y_pred, color='red', label='Trend Line')  # Línea de regresión
        plt.title("Pace Through the Days")
        plt.xlabel("Date")
        plt.ylabel("Pace (minutes per km)")
        plt.legend()
        plt.xticks(rotation=45)  # Rotar fechas para mejor legibilidad
        plt.grid(True)
        plt.show()
