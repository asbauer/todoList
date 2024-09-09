import json
import os

def menu():
    while True :
        print("To-Do List: ")
        view_tasks()
        print("\n Options")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = None
        while choice is None :
            try :
                choice = int(input("Please choose an option"))
            except :
                print("Please only enter a number from the options")
            
