import pandas as pd
import os

csv = "./csv/savefile.csv"

class Save():
    dataToSave = {"Pace","Date","Distance","Time"}

    def setPace(self,pace):
        if isinstance(pace,float):
            return pace
        else:
            return float(pace)
    
    def setDate(self, date):
        PandasDate = pd.Timestamp(date)

        # Formato con horas y minutos
        formatted_Date = PandasDate.strftime("%Y-%d-%m %H:%M")

        return formatted_Date  # Devuelve la fecha formateada con horas y minutos

    
    def setDistance(self,distance):
        if isinstance(distance,int):
            return distance
        else:
            return int(distance)
        
    def setTime(self, time):
        if isinstance(time,float):
            return time
        else:
            return float(time)
            

    def __init__(self,pace,date,distance,time):
        self.Pace = self.setPace(pace)
        self.Date = self.setDate(date)
        self.Distance = self.setDistance(distance)
        self.Time = self.setTime(time)

        self.dataToSave= {"Pace": self.Pace,
                          "Date": self.Date,
                          "Distance":self.Distance,
                          "Time":self.Time
        }
    
    def SaveToCSV(self):
        df = pd.DataFrame([self.dataToSave])

        if not os.path.exists(csv):
            df.to_csv(csv, index=False)
            print("Creating File...")
        else:
            df.to_csv(csv, mode='a', header=False, index=False)
            print("Saving")



