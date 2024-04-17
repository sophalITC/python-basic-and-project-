from Db import add_habit


class Add: # Add class, to add Habits
    
    def __init__(self, Date: str,Habit_name: str, Frequency: str ,To_Do: str,Duration: str): 
        
        self.Date = Date
        self.Habit_name = Habit_name
        self.Frequency = Frequency
        self.To_Do = To_Do
        self.Duration = Duration
        
    def store(self, conn): # Add habits into the habit table database
        
        add_habit(conn, self.Date, self.Habit_name, self.Frequency, self.To_Do, self.Duration)
                
    
        