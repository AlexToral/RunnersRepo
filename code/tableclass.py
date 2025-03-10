import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
import time
import threading


class Table():

    def update_df_if_needed(self):
        """Check if the CSV file has been modified, and reload it if necessary."""
        current_modified = os.path.getmtime(self.csv)
        if current_modified != self.last_modified:  # If the file has changed
            self.df = pd.read_csv(self.csv)  # Reload the DataFrame
            self.last_modified = current_modified  # Update the last modified time
            print("CSV file updated!")

    def start_periodic_update(self, interval=5):
        """Start the periodic update check every `interval` seconds using threading."""
        def update_loop():
            while True:
                self.update_df_if_needed()  # Check and update the DataFrame
                time.sleep(interval)  # Wait for the specified interval
        
        # Start the update loop in a new thread
        threading.Thread(target=update_loop, daemon=True).start()

    def __init__(self):
        self.csv = "./csv/savefile.csv"
        #if the file is not found, create it
        if not os.path.exists(self.csv):
            self.df = pd.DataFrame(columns=["Pace","Date","Distance","Time"])
            self.df.to_csv(self.csv, index=False)   

        self.df = pd.read_csv(self.csv)
        self.last_modified = os.path.getmtime(self.csv)
    
    def minPace(self):
        self.start_periodic_update()
        try:
            minpace = min(self.df["Pace"])
            return minpace
        except:
            return "No data"
    
    def maxDistance(self):
        self.start_periodic_update()
        try:
            maxDistance = max(self.df["Distance"])
            return maxDistance
        except:
            return "No data"

    def graphDateandPace(self):
        self.start_periodic_update()

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

    def graphDateandDistance(self):
        self.start_periodic_update()
         # Convertir 'Date' a tipo datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')

        # Eliminar filas con valores NaN en 'Date' o 'Pace'
        self.df = self.df.dropna(subset=['Date', 'Distance'])

        # Convertir fechas a valores numéricos
        self.df['Date_numeric'] = (self.df['Date'] - self.df['Date'].min()) / pd.Timedelta(days=1)

        # Definir variables de regresión
        X = self.df['Date_numeric'].values.reshape(-1, 1)  # Features (dates)
        y = self.df['Distance'].values  # Target (pace)

        # Ajustar modelo de regresión lineal
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        # Graficar
        plt.figure(figsize=(10, 5))
        plt.scatter(self.df['Date'], self.df['Distance'], color='blue', label='Data Points')  # Scatter plot
        plt.plot(self.df['Date'], y_pred, color='red', label='Trend Line')  # Línea de regresión
        plt.title("Distance Through the Days")
        plt.xlabel("Date")
        plt.ylabel("Distance (meters)")
        plt.legend()
        plt.xticks(rotation=45)  # Rotar fechas para mejor legibilidad
        plt.grid(True)
        plt.show()