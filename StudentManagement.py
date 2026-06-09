import json # To access json.load() and json.dump()
import os #TO clear the terminal
import time #TO give a seconds delay

def main_menu(): # Main menu just the decoration
    print("=" * 32)
    print("=======Student Management=======")
    print("=" *32)
    print("            Main Menu           ")
    print("=" *32)
    print("1. Add Student \n2. View All Students \n3. Search Student \n4. Update Student Marks \n5. Delete Student \n6. Exit")
    print("=" *32)

def add_student(): #Function 2 where students info gets added
    global info # Creates a dictionary that will be dumped into the JSON file 
    info = {}
    check = {}

    with open(file_name , "r") as file: # Tries reading the file in read mode 
        try:
            check = json.load(file) # Loads the JSON data into the 'check' dictionary
        except:# If the file is empty, keep check as an empty dictionary
            pass

    Student_ID = input("Enter student ID : ")

    while True: 
        while not Student_ID.isdigit(): # Ensure the Student ID contains only digits
            print("Student ID must contain numbers only!")
            
        while Student_ID in check: # Checks whether the Student ID already exists
            print("This ID is already taken")

        else:
            break
        
        Student_ID = input("Enter student ID : ")
        
    name = input("Enter student name : ")
    Class = input("Enter Class : ")
    marks = input("Enter your marks : ")
    data = {
        "Name" : name,
        "Class" : Class,
        "Marks" : marks
    }  #Here the entire data is the value and the student id is the key 
    info[Student_ID] = data # Key(Student_ID) : value(data)

def Get_ID(): # Function 3 where the user enters a Student ID
    global ID , data
    ID = (input("Enter Student ID: "))
    try: 
        with open(file_name , "r") as file: # Tries reading the file in read mode 
            file.seek(0)
            data = json.load(file) # Loads the existing data 
    except: #If error comes no data found
        print("No student found!")
    
file_name = "Student_Management_System.json" # JSON file where the data store

try:
    while True: #Main LOOP of the program AKA Student Management System
        os.system("cls") #Clears the Terminal before running 
        main_menu() 

        user_input = input("Enter choice : ") #Users choice to Add student Remove student stuff like that
        while user_input not in {"1" , "2" , "3" ,"4" , "5" , "6"}: #If user enters a invalid option 
            print("Invalid option")
            user_input = input("Enter choice : ")

        if user_input == "1" : # For ADD student 
            if os.path.exists(file_name): #Checks if the file exists or not 
                with open(file_name , "r+") as file: #File exists open in r+ mode

                    try: 
                        file.seek(0)
                        details = json.load(file) #Try reading the file is the file is empty a error pops

                    except: #Handels the error
                        add_student() # Add new student 
                        json.dump(info , file , indent= 4) #DUMP in the file

                    else: #If old the file as old data 
                        add_student() # Add new student
                        with open(file_name , "w+") as file2: #open in W+ mode to clear the file
                            info.update(details) #DO OLD + NEW DATA 
                            json.dump(info , file2 , indent= 4) #DUMP
                    
            else: #IF file does't exists open in w+ mode to create a file 
                with open(file_name , "w+") as file: #open in w+ mode
                    add_student() # Add new student
                    json.dump(info , file , indent= 4) #DUMP

        elif user_input == "2": # For viewing all students
            try: #TRY reading the file 
                with open(file_name , "r") as file: # Tries reading the file in read mode
                    file.seek(0)
                    data = json.load(file) # Loads the existing data 
            except: #If its error occur then no data found
                print("NO student data found")
            else: #If the data load 
                for ID  , info in data.items(): # Traverse through all student records
                    print(ID , info)

        elif user_input == "3": # For searching a particular student's data
            Get_ID() #Here we will get the ID of a perticular student
            if ID in data: #Check if the ID is found in data varibles 
                print(data[ID]) #Print the student data
            else: #if not then no data found
                print("No student found!")
                
        elif user_input == "4": #For updating the data of a perticular student 
            Get_ID() #Here we will get the ID of a perticular student
            if ID in data: #Check if the ID is found in data varibles
                change = input("What do you want to change (Name/Class/Marks): ").title() # Ask the user what field to update
                while change not in {"Name" , "Class" , "Marks"}: #if the input is not in this 3
                    print("Invalid option") 
                    change = input("What do you want to change (Name/Class/Marks): ").title() 
                Update = input("Enter updated value: ") #Enters the updated value
                data[ID][change] = Update #value gets updated in the data
                with open(file_name , "w+") as file: #Files gets open in w+ mode
                    json.dump(data , file , indent= 4) #DUMP
            else: #if not then no data found
                print("No student found!")

        elif user_input == "5": #For deleting a perticular student data
            Get_ID() #Here we will get the ID of a perticular student
            if ID in data: #Check if the ID is found in data varibles
                del data[ID] # Delete the student record from the data
                with open(file_name , "w+") as file: #open the file in w+ mode
                    json.dump(data , file , indent= 4) #DUMP
            else: #if not then no data found
                print("No student found!")
        else: #Exit the program from main loop
            print("Thanks for Running the program")
            break

        time.sleep(1.5) #Takes a 1.5 second break 
        os.system("cls") # Clears the terminal

except KeyboardInterrupt: # Handle Ctrl + C (KeyboardInterrupt) gracefully
    print("\nThanks for Running the program")