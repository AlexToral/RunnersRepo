
from customtkinter import *
from GUI.SAVEGUI import SaveGui
from datetime import datetime
from tableclass import Table

class App(CTk):

    def refetch_data(self):
    
        # Refetch or update any data you need here
        self.update_event_countdown()
        self.minPace()
        self.maxDistance()
        
        self.after(1000, self.refetch_data)

    def open_save_window(self):
        self.save_window = SaveGui(self)

    def update_event_countdown(self):
        today = datetime.now()
        delta = self.event_date - today

    # Extract the number of days and the remaining seconds
        days = delta.days
        remaining_seconds = delta.seconds

    # Calculate hours and minutes from the remaining seconds
        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60


    # Update the display without seconds or milliseconds
        self.DAYS.configure(text=f"{days} Days {hours} Hours")
    
    def open_Pace_Days_Graph(self):
        self.table.graphDateandPace()

    def open_Distance_Days_Graph(self):
        
        self.table.graphDateandDistance()

    def minPace(self):
        min =  self.table.minPace()
        self.PacePR.configure(text=min)

    def maxDistance(self):
        max =  self.table.maxDistance()
        self.DistancePR.configure(text=max)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table = Table()

        self.Title = CTkLabel(master=self, text="Welcome\nTo\nRunner Stats", font=CTkFont(size=45, weight="bold"))
        self.Title.pack()

        self.buttonframe = CTkFrame(master=self, bg_color=("gray92", "#14142b"), fg_color=("gray90", "#14142b"))
        self.buttonframe.pack_propagate(False)
        self.buttonframe.pack(fill="both")

        self.SaveWindow = CTkButton(master=self.buttonframe, text="Save Progress\n", height=0, compound="bottom", anchor="s", fg_color=("#3a7ebf", "#9b529c"), bg_color="transparent", hover_color=("#325882", "#623463"), state="normal", border_spacing=0, corner_radius=10, font=CTkFont(family="@UD Digi Kyokasho NK", weight="bold", size=18),command=self.open_save_window)
        self.SaveWindow.pack(pady=(20, 0), fill="x")

        self.PaceGraph = CTkButton(master=self.buttonframe, text="Show Pace through time\n", height=10, compound="top", anchor="center", fg_color=("#3a7ebf", "#9b529c"), hover_color=("#325882", "#623463"), corner_radius=10, font=CTkFont(family="@UD Digi Kyokasho NK", weight="bold", size=18),command=self.open_Pace_Days_Graph)
        self.PaceGraph.pack(fill="x", pady=(20, 0))

        self.DistanceGraph = CTkButton(master=self.buttonframe, text="Show Distance through time\n", height=10, compound="top", anchor="center", fg_color=("#3a7ebf", "#9b529c"), hover_color=("#325882", "#623463"), corner_radius=10, font=CTkFont(family="@UD Digi Kyokasho NK", weight="bold", size=18),command=self.open_Distance_Days_Graph)
        self.DistanceGraph.pack(fill="x", pady=(20, 0))

        self.FramePR = CTkFrame(master=self, fg_color=("gray90", "#14142b"), bg_color="transparent")
        self.FramePR.pack_propagate(False)
        self.FramePR.pack(fill="both")

        self.DistanceFrame = CTkFrame(master=self.FramePR, height=200, width=250, corner_radius=0, fg_color=("gray85", "#14142b"))
        self.DistanceFrame.pack_propagate(False)
        self.DistanceFrame.pack(side="left")

        self.DistancePRTitle = CTkLabel(master=self.DistanceFrame, text="Distance PR:", fg_color="transparent", width=200, corner_radius=0, padx=34, justify="left", compound="left", anchor="center", height=10, font=CTkFont(size=30, weight="normal"))
        self.DistancePRTitle.pack(padx=(0, 81))

        self.DistancePR = CTkLabel(master=self.DistanceFrame, text=f"NA", width=250, height=200, compound="left", justify="left", padx=0, font=CTkFont(family="@Microsoft YaHei Light", size=65))
        self.DistancePR.pack(padx=(0, 78))

        self.PaceFrame = CTkFrame(master=self.FramePR, width=250, corner_radius=0, bg_color=("gray90", "#14142b"), fg_color=("gray85", "#14142b"))
        self.PaceFrame.pack_propagate(False)
        self.PaceFrame.pack(side="right")

        self.PacePRtitle = CTkLabel(master=self.PaceFrame, text="Pace PR:", font=CTkFont(size=45, weight="normal"))
        self.PacePRtitle.pack(padx=(40, 0))

        self.PacePR = CTkLabel(master=self.PaceFrame, text=f"NA", width=200, height=200, font=CTkFont(family="@Microsoft YaHei Light", size=65))
        self.PacePR.pack(padx=(123, 0))

        self.EventFrame = CTkFrame(master=self, fg_color=("gray90", "#14142b"))
        self.EventFrame.pack_propagate(False)
        self.EventFrame.pack(fill="x")

        self.NextEvent = CTkLabel(master=self.EventFrame, text="Next Event", font=CTkFont(size=45, weight="bold"))
        self.NextEvent.pack()

        self.event_name = CTkLabel(master=self.EventFrame, text="Half Marathon", font=CTkFont(size=15, weight="normal"))
        self.event_name.pack()
        
        self.DAYS = CTkLabel(master=self.EventFrame, text="70 Days", font=CTkFont(size=45, weight="normal"))
        self.DAYS.pack()

        self.event_date = datetime(2025,5,18,6,00,00)
        self.update_event_countdown()
        self.refetch_data()
        
        
