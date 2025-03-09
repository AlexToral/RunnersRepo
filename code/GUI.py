import tkinter as tk
from tkinter import messagebox
from savefile import Save 
def save_data():
    try:
        # Get input data from entry fields
        pace = float(pace_entry.get())
        date = date_entry.get()
        distance = int(distance_entry.get())
        time = float(time_entry.get())

        # Create a new Save object
        new_data = Save(pace, date, distance, time)

        # Save data to CSV
        new_data.SaveToCSV()

        # Show a success message
        messagebox.showinfo("Success", "Data saved successfully!")

        # Optionally clear the input fields after saving
        pace_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        distance_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

    except ValueError as e:
        # Handle invalid input (e.g., non-numeric values)
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Save Data to CSV")
root.geometry("300x300")

# Create labels and entry fields for the input
tk.Label(root, text="Pace:").pack(pady=5)
pace_entry = tk.Entry(root)
pace_entry.pack(pady=5)

tk.Label(root, text="Date (YYYY-DD-MM):").pack(pady=5)
date_entry = tk.Entry(root)
date_entry.pack(pady=5)

tk.Label(root, text="Distance (in meters):").pack(pady=5)
distance_entry = tk.Entry(root)
distance_entry.pack(pady=5)

tk.Label(root, text="Time (in minutes):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

# Create a button to save the data
save_button = tk.Button(root, text="Save Data", command=save_data)
save_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
