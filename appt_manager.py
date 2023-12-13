# Group 9 - (Gordon) Chi Wai Tsui, (Sam) Ho Sum Chan, Grantly Tong
# Date 08-Dec-2023


# import appointment as ap for the Class "Appointment" and its method
import appointment as ap
# import os module for checking the file exist or not
import os

# define the weekly calendar to save the appointment objects
weekly_calendar = []
# define the days and available hours for the object attributes.
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
available_hours = [9, 10, 11, 12, 13, 14, 15, 16]


def create_weekly_calendar():  
    '''
    1. Iterates through each day of the week (Monday to Saturday)
    2. For each day, iterates through each available hour (9 to 16)
    3. For each hour, creates new Appointment object and adds it to the appointment list (i.e. calendar)
    '''
    for day in days_of_the_week:
        for hour in available_hours:
            appt = ap.Appointment(day, hour)
            weekly_calendar.append(appt)
    return weekly_calendar

def find_appointment_by_time(day_of_week, start_time_hour):  
    '''
    1. Receives the day and start hour of the appointment to find
    2. Searches the list of Appointments for corresponding day and start hour
    3. If the appointment is found, returns the Appointment object, otherwise returns nothing
    '''
    for appointment in weekly_calendar:
        if appointment.get_day_of_week().capitalize() == day_of_week.capitalize():
            if appointment.get_start_time_hour() == start_time_hour:
                return appointment

def load_scheduled_appointments():  
    '''
    1. Inputs appointment filename from user
    2. Iterates over each line (i.e. appointment) in the file, parsing the attribute values into separate variables
    3. Calls find_appointment_by_time() to locate the corresponding appointment in the list and invoke the schedule() method to set the properties appropriately
    4. Returns the number of scheduled appointments loaded
    '''
    # Get user input to confirm if they want to import the data from previous file
    load = input("Would you like to load previously scheduled appointments from a file (Y/N)? ")
    if load.upper() == "Y":
        fileOpen = input("Enter appointment filename: ")
        # check if the file name exist or not using the os module, if not, user need to re-enter until it is correct
        # Better to consider a exit mechanism in case user just wrongly type "y", otherwise it has to kill the program to restart.
        while os.path.exists(fileOpen) == False:
            fileOpen = input("File not found. Re-enter appointment filename: ")
        else:
            # open up the file as read only
            openUp = open(fileOpen, "r")
            # declare the apptointment number read as 0 first
            appt_num = 0
            for info in openUp.readlines():
                # using rstrip() to remove the '\n' at the end of each line
                info = info.rstrip("\n")
                # split menthod to get the readline into a list by separate it with each comma
                appt = info.split(",")
                # assign the value to variable
                client_name = appt[0]
                client_phone = appt[1]
                appt_type = int(appt[2])
                day_of_week = appt[3]
                start_time_hour = int(appt[4])
                # for each record read, the appointment number is added
                appt_num += 1
                # to find out the appointment in weekly_calander list which was created at the beginning of main function by using find_appointment_by_time function below
                booking = find_appointment_by_time(day_of_week, start_time_hour)
                # set the attributes to class using Appointment class method
                booking.schedule(client_name, client_phone, appt_type)
            # close the file after completed the for loop
            openUp.close()
            print(f"{appt_num} previously scheduled appointments have been loaded")

def print_menu(): 
    '''
    1. Displays the menu of application options
    2. Accepts menu selection from user until valid selection is entered
    3. Returns user’s valid selection
    '''
    print("\n\nJojo's Hair Salon Appointment Manager")
    print("=" * 37)
    print(" 1) Schedule an appointment")
    print(" 2) Find appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) Cancel an appointment")
    print(" 9) Exit the system")
    # Global the variable here so it can be used in main function while loop.
    global userchoice
    userchoice = int(input("Enter your selection: "))

def show_appointments_by_name(): 
    '''
    1. Receives the client name of the appointment(s) to show
    2. Searches the list of Appointments for corresponding client name, allowing for partial & non-case sensitive matches
    3. Displays all matching appointments in the format given in the Sample Run (hint: use the __str__() method implicitly)
    '''
    # initialize a variable "flag" to 0. It will be used later to check if any appointments are found.
    flag = 0
    print("\n** Find appointment by name**")
    client_name = input("Enter Client Name: ")
    print("Appointments for ", client_name, "\n")
    print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name","Phone", "Day", "Start", "End", "Type"))
    print("-"*85)
    # iterates through each appointment in the "weekly_calendar"
    for appt in weekly_calendar:
        #checks whether the entered client name is a string of client name in the current appointment or not
        if client_name.lower() in appt.get_client_name().lower():
            print(appt)
            #sets the flag to "1" to indicate that there is appointed already
            flag = 1
    # no appointments were found if it is still "0"
    if flag == 0:
        print("No appointments found.")

def show_appointments_by_day(): 
    '''
    1. Receives the day of the appointments to show
    2. Searches the list of Appointments for the corresponding day
    3. Displays all matching appointments in the format given in the Sample Run (hint: use the __str__() method implicitly)
    '''
    print("\n** Print calendar for a specific day **")
    day = input("Enter day of week: ")
    print("Appointments for ", day.capitalize(), "\n")
    print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name","Phone", "Day", "Start", "End", "Type"))
    print("-"*85)
    # iterates through each appointment in "weekly_calendar"
    for appt in weekly_calendar:
        # checks whether the entered day match the day of the current appointments. It it matches, print the appointment details
        if appt.get_day_of_week().capitalize() == day.capitalize():
            print(appt)
    
def save_scheduled_appointments():  
    '''
    1. Inputs appointment filename from user, checks if the file already exists and if so, allows user to proceed (i.e. overwrite the file) or repeat the filename input
    2. Iterates over each appointment in the list and if scheduled (i.e. appt_type != 0), writes the appointment to the file in the proper CSV format (hint: use the format_record() method)
    3. Returns the number of scheduled appointments saved
    '''
    # Ask for user input if they want to save the appointments data
    saveFile = input("Would you like to save all scheduled appointments to a file (Y/N)?")
    if saveFile.upper() == "Y":
        # ask user input for the file name
        fileName = input("Enter appointment filename: ")
        # declare the record wrote in the file
        rec = 0
        # using os module to check if the file is existed or not.
        if os.path.exists(fileName):
            # confirm with client if they want to overwrite the file
            confirm = input("File already exists. Do you want to overite it (Y/N)?")
            if confirm.upper() == "Y":
                # using "w" method to overwrite all the existing data in the file.
                f = open(fileName, "w")
                for appt in weekly_calendar:
                    # since created the calendad included all the appointment object for all days all time slot no matter it has appointment or not. Thus here need to check if there is client name exist, only if client name data is not null (mean a confirmed booking) will be record in the file.
                    if appt.get_client_name() != "":
                        f.write(appt.format_record())
                        # to confirm each entry will be in a new line. also align with the load appointment function coding.
                        f.write("\n")
                        # add 1 record for each entry
                        rec += 1
                f.close()
                print(f"{rec} scheduled appointments have been successfully saved\nGood Bye!")
            else:
                fileName = input("Enter appointment filename: ")
                f = open(fileName, 'w')
                for appt in weekly_calendar:
                    if appt.get_client_name() != "":
                        f.write(appt.format_record())
                        f.write("\n")
                        rec += 1
                f.close()
                print(f"{rec} scheduled appointments have been successfully saved\nGood Bye!")
        else:
            f = open(fileName, "w")
            for appt in weekly_calendar:
                if appt.get_client_name() != "":
                    f.write(appt.format_record())
                    f.write("\n")
                    rec += 1
            f.close()
            print(f"{rec} scheduled appointments have been successfully saved\nGood Bye!")


def cancel_appointment():  
    '''
    Cancel appointment with user input the appointment name
    '''
    print("** Cancel an appointment **")
    day = input("What day: ")
    hour = int(input("Enter start hour (24 hour clock): "))
    for appt in weekly_calendar:
        if appt.get_day_of_week().capitalize() == day.capitalize():
            if appt.get_start_time_hour() == hour:
                if appt.get_client_name() == "":
                    print("That time slot isn't booked and doesn't need to be cancelled!\n")
                else:
                    print("Appointment: ", day, hour, ":00 - ",hour + 1, ":00 for ", appt.get_client_name(), " has been cancelled!\n")
                    appt.cancel()
                return
    print("Sorry that time slot is not in the weekly calendar!\n")


def schedule_appointment(): 
    '''
    Making appointment as per using input
    '''
    print("\n** Schedule an appointment **")
    day_of_week = input("What day: ")
    start_time_hour = int(input("Enter start hour (24 hour clock): "))

    if day_of_week.capitalize() not in days_of_the_week or start_time_hour not in available_hours:
        print("Sorry that time slot is not in the weekly calendar!")
        # simply ask for user input and then using schedule method to save the appointment.

    # check if the provided day and time slot has other client appointment or not by checking the client_name attribute.
    elif find_appointment_by_time(day_of_week, start_time_hour).get_client_name() != '':
        print("Sorry that time slot is booked already!")
    # for the incorrect input of day or hours, return the fail message.
    # note that both failure condition will return to main menu instead of asking for reenter
    else:
        client_name = input("Client Name: ")
        client_phone = input("Client Phone: ")
        print("Appointment types")
        appt_type = int(input(
            "1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120\nType of Appointment: "))
        if appt_type > 4 or appt_type < 1:
            print("Sorry that is not a valid appointment type!")
        else:
            appt = find_appointment_by_time(day_of_week, start_time_hour)
            appt.schedule(client_name, client_phone, appt_type)
            print(f"OK, {client_name}'s appointment is scheduled!")


def main(): 
    '''
    1. Entry point for the Appointment Management System
    2. Coordinates the overall processing:
        A. Set up a list of appointments for the week
        B. Optionally load a previous appointment schedule
        C. Present the menu, get and evaluate user’s selection, repeating until user chooses to quit:
            i. Get additional user inputs as needed
            ii. Call appropriate functions and/or Appointment class methods to help perform the actions for each menu option
            iii. Display relevant context/status messages
        D. Optionally save scheduled appointments to a file before ending program
    '''
    print("Starting the Appointment Manager System")
    # create the weekly schedule first
    create_weekly_calendar()
    print("Weekly calendar created!")
    # load the scheudle appointments
    load_scheduled_appointments()
    print_menu()
    # ask for user input again if they do a wront input
    while userchoice not in [1, 2, 3, 4, 9]:
        print("Sorry that is not a valid appointment type!")
        print_menu()
    # if the user keep enter the number, the progrm will continue running until they enter "9" and trigger exit() function
    while userchoice:
        match userchoice:
            case 1:
                schedule_appointment()
                print_menu()
            case 2:
                show_appointments_by_name()
                print_menu()
            case 3:
                show_appointments_by_day()
                print_menu()
            case 4:
                cancel_appointment()
                print_menu()
            case 9:
                print("** Exit the system **")
                save_scheduled_appointments()
                exit()


if __name__ == "__main__":
    main()

