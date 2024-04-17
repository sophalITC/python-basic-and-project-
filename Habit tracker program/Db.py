import sqlite3 # This module is to integrate SQlite database with python
import pandas as pd # this module is for analyzing, cleaning, exploring, and manipulating data
from tabulate import tabulate # this module is to present data in a visually appealing table format
import numpy as np # this module is for Mathematical operations on arrays

def get_db(name="main.db"): # This function is for creating the database file

    conn = sqlite3.connect(name)
    create_tables(conn)
    return conn


def create_tables(conn): # This function is for creating a database table

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
            Date TEXT,
            Habit_name TEXT,
            Frequency TEXT,
            To_Do TEXT,
            Duration TEXT)""")


    conn.commit()

def add_habit(conn,Date,Habit_name, Frequency,To_Do,Duration): # This function is for add the data that are obtained from 'Main.py' and Insert it in the habits table
    
    cur = conn.cursor()
   
    cur.execute("INSERT OR REPLACE INTO habits VALUES (?, ?, ?, ?, ?)", (Date, Habit_name, Frequency, To_Do, Duration))
    

    conn.commit()
    
def habit(conn): # This function is for printing the Habit table that display all saved habit including Date, Habit name, Frequency, Do at time, Duration 
    
    sql = pd.read_sql_query("SELECT * FROM habits", conn)
    df = pd.DataFrame(sql)
    df.index = np.arange(1, len(df) + 1)
    headers = ["Date","Habit Name", "Frequency", "Do at Time", "Duration"]
    print(tabulate(df, headers, tablefmt="fancy_grid"))
    
