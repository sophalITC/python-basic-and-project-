import questionary # This module is for displaying multiple option for user to pick and get user input
import datetime # This module is for time
from Db import get_db,habit # Get Functions from The 'Db.py'file
from Add_habit import Add # Get class Add from the 'Add_habit'file


def greeting(): # This function is for displaying a welcome message
    
    currentTime = datetime.datetime.now()
    currentTime.hour # Only Get the hour value of the current time
    
    if currentTime.hour < 12: 
        print('  "Good morning"')
    elif 12 <= currentTime.hour < 18:
        print('  "Good afternoon"')
    else:
        print('  "Good evening"')
greeting()
           
                     
def Choose(): # This function is for get data from a user by choosing the given option

    conn = get_db()
    
    while True:
        
        global Habit_name # Global variable so it can be used in different function
        
        choice = questionary.select("Choose What you would like to do: ",
                                    choices = ["1. Create a new habit",
                                            "2. Habit list",
                                            "3. Exit"]).ask()
        if choice == "3. Exit": # This will Stop the loop and end the program
            
            print("     Goodbye")
            
            break
        
        elif choice == "1. Create a new habit":
            
            choice = questionary.select("Choose",
                                    choices = ["1. Sleep Schedule",
                                                "2. Block screen time",
                                                "3. Limit caffeine intake",
                                                "4. Intermittent fasting",
                                                "5. Read a book",
                                                "6. No alcohol",
                                                "7. Exercise",
                                                "8. Create your own habit",
                                                "9. Exit"]).ask()
            
            if choice == "1. Sleep Schedule":
                Habit_name = "Sleep Schedule"
                question() 
                
            elif choice == "2. Block screen time":
                Habit_name = "Block screen time"
                question()
                
            elif choice == "3. Limit caffeine intake":
                Habit_name = "Limit caffeine intake"
                question()
                
            elif choice == "4. Intermittent fasting":
                Habit_name = "Intermittent fasting"
                question()
                
            elif choice == "5. Read a book":
                Habit_name = "Read a book"
                question()
                
            elif choice == "6. No alcohol":
                Habit_name = "No alcohol"
                question()
                
            elif choice == "7. Exercise":
                Habit_name = "Exercise"
                question()
                
            elif choice == "8. Create your own habit":
                Habit_name = input("Enter a habit name: ")
                question()
        
        elif choice == "2. Habit list": # Return all habits in the form of data table
            habit(conn)
            
            
def question(): # This function is for getting data from user by asking them question and letting them pick the given option and make their own
    
    conn = get_db() # Calling a function from another py file to connect to the Database 
    
    Date = datetime.datetime.now().year # To display current year that a habit was given by user

    Frequency = questionary.select("Frequency of Habit: ",  
                                                    choices = ["Daily",
                                                            "Weekly",
                                                            "Monthly"]).ask()
                        
                        
    To_do = questionary.select("Choose time: ",
                                                        choices = ["Anytime",
                                                                "Morning",
                                                                "Afternoon",
                                                                "Evening",
                                                                "Night"]).ask()

    Duration = questionary.select("Duration: ",
                                                choices=["10 Minutes",
                                                        "20 Minutes",
                                                        "30 Minutes",
                                                        "40 Minutes",
                                                        "50 Minutes",
                                                        "1 hour",
                                                        "Custom time"]).ask() 
    if Duration == "Custom time":
                            Duration = input("Enter Custom time: ")

    print("Your habit have been created successfully!")
    
    Add_habit = Add(Date, Habit_name, Frequency,To_do,Duration)
    
    Add_habit.store(conn) # Store the Habit Data in the Database
                        
Choose() # Call function to start the program

