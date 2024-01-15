import os
from datetime import datetime
import keyboard

class track():
    def __init__(self,name):
        self.name = name
        self.filepath = self.name + ".csv"
        self.shortcut_note = "ctrl+alt+f"

        if os.path.exists(self.filepath):
            print("A file with this podcast name already exists. You can still append notes to this file though.")
            import pandas as pd
            df = pd.read_csv(self.filepath)
            df["Datetime"] = pd.to_datetime(df['Datetime'])
            self.start_time = df["Datetime"].min().to_pydatetime()
            self.id = df["ID"].max()
        else:        
            self.start_time = datetime.now()
            self.id = 0
            try:
                with open(self.filepath, "w") as file:
                    file.write(f"ID,Datetime,Time Delta,Note\n{self.id},{self.start_time},0,Started podcast for {self.name}")
                    print("File initiated")
            except:
                print("Error: could not create file.")
                

    def time_difference(self,start,end):
        diff = end - start

        # Extract hours, minutes, and seconds from the time difference
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        formatted_difference = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return formatted_difference

    def note(self,*notes):
        if notes:
            txt = " ".join(notes)
        else:
            txt = input(f"Please enter your note for {self.id+1}: ")
            if txt == None or txt.strip() == "":
                print("No text was given")
                return
        
        self.id += 1
        ts = datetime.now()
        delta = self.time_difference(self.start_time,ts)
        try:
            with open(self.filepath, "a") as file:
                file.write(f"\n{self.id},{ts},{delta},{txt}")
            print(f"Note added with ID {self.id}")
        except:
            print("Error: Could not write the note")

    # function to keep taking notes until user types exit
    def takenotes(self):
        while True:
            txt = input(f"Please enter your note for {self.id+1}, or type exit: ")
            if txt == "exit":
                break
            else:
                self.note(txt)