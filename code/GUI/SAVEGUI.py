
from customtkinter import *
import savefile as save
import tkinter as tk



   
class SaveGui(CTkToplevel):
   
   def close_window(self):
       self.destroy()
       
   def save_data(self):
        # Get input data from entry fields
        pace = float(self.pace_entry.get())
        date = self.date_entry.get()
        distance = int(self.distance_entry.get())
        time = float(self.time_entry.get())

        # Create a new Save object
        new_data = save.Save(pace, date, distance, time)

        # Save data to CSV
        new_data.SaveToCSV()

        # Show a success message

        # Optionally clear the input fields after saving
        self.pace_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.distance_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)



   def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent  
        self.title("Save Window")
        self.geometry("500x500")
        self.configure(fg_color=('gray92', '#14142b'))

        self.FRAME1 = CTkFrame(master=self, height=299, fg_color=("gray86", "#14142b"))
        self.FRAME1.pack_propagate(False)
        self.FRAME1.pack(fill="x")

        self.PaceLabel = CTkLabel(self.FRAME1, text="Pace:", font=CTkFont(size=35))
        self.PaceLabel.pack()
        self.pace_entry = CTkEntry(self.FRAME1, placeholder_text="MM.SS", justify="center", width=225)
        self.pace_entry.pack()

        self.Date = CTkLabel(self.FRAME1, text="Date:", font=CTkFont(size=35))
        self.Date.pack()
        self.date_entry = CTkEntry(self.FRAME1, placeholder_text="YYYY-MM-DD HH:MM:SS", justify="center", width=225)
        self.date_entry.pack()

        self.DistanceLabel = CTkLabel(self.FRAME1, text="Distance:", font=CTkFont(size=35))
        self.DistanceLabel.pack()
        self.distance_entry = CTkEntry(self.FRAME1, placeholder_text="in meters", justify="center", width=225)
        self.distance_entry.pack()

        self.TimeLabel = CTkLabel(self.FRAME1, text="Time:", font=CTkFont(size=35))
        self.TimeLabel.pack()
        self.time_entry = CTkEntry(self.FRAME1, placeholder_text="in minutes", justify="center", width=225)
        self.time_entry.pack()

        # Frame para los botones
        self.FRAME10 = CTkFrame(self, height=100, fg_color=("#14142b", "#14142b"))
        self.FRAME10.pack(fill="x", pady=10)

        self.save_button = CTkButton(self.FRAME10, text="Save", command=self.save_data)
        self.save_button.pack(pady=10)

        self.home_button = CTkButton(self.FRAME10, text="Home", command=self.close_window)
        self.home_button.pack()

        self.lift()  # This raises the window to the top layer
        self.attributes("-topmost", True)  # Keeps the window always on top

