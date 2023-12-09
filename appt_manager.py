import appointment as ap
appt_list={}
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def create_weekly_calendar():#Nam
    '''
    1. Iterates through each day of the week (Monday to Saturday)
    2. For each day, iterates through each available hour (9 to 16)
    3. For each hour, creates new Appointment object and adds it to the appointment list (i.e. calendar)

    '''



create_weekly_calendar()
def find_appointment_by_time(day_of_week,start_time_hour):#Nam
    '''
    1. Receives the day and start hour of the appointment to find
    2. Searches the list of Appointments for corresponding day and start hour
    3. If the appointment is found, returns the Appointment object, otherwise returns nothing

    '''


def load_scheduled_appointments():#Gordon
    '''
    1. Inputs appointment filename from user
    2. Iterates over each line (i.e. appointment) in the file, parsing the attribute values into separate variables
    3. Calls find_appointment_by_time() to locate the corresponding appointment in the list and invoke the schedule() method to set the properties appropriately
    4. Returns the number of scheduled appointments loaded
    '''
    fileOpen = input("Enter appointment filename: ")
    openUp = open(fileOpen, "r")
    appt_num=0
    for info in openUp.readlines():
        info = info.rstrip("\n")
        appt = info.split(",")
        client_name = appt[0]
        client_phone = appt[1]
        appt_type = int(appt[2])
        day_of_week = appt[3]
        start_time_hour = int(appt[4])
        appt_num +=1
        find_appointment_by_time(day_of_week,start_time_hour)
        appt_list[day_of_week][start_time_hour]=ap.Appointment(day_of_week,start_time_hour)
        appt_list[day_of_week][start_time_hour].schedule(client_name,client_phone,appt_type)
    openUp.close()
    print(f"{appt_num} previously scheduled appointments have been loaded")

def print_menu():#individual work
    '''
    1. Displays the menu of application options 
    2. Accepts menu selection from user until valid selection is entered
    3. Returns user’s valid selection

    '''
    print ("Jojo's Hair Salon Appointment Manager")
    print ("="*37)
    print (" 1) Schedule an appointment")
    print (" 2) Find appointment by name")
    print (" 3) Print calendar for a specific day")
    print (" 4) Cancel an appointment")
    print (" 9) Exit the system")
    global userchoice 
    userchoice= int(input("Enter your selection: "))

def show_appointments_by_name(): #Sam
    '''
    1. Receives the client name of the appointment(s) to show
    2. Searches the list of Appointments for corresponding client name, allowing for partial & non-case sensitive matches
    3. Displays all matching appointments in the format given in the Sample Run (hint: use the __str__() method implicitly)

    '''


def show_appointments_by_day(): #Sam
    '''
    1. Receives the day of the appointments to show
    2. Searches the list of Appointments for the corresponding day
    3. Displays all matching appointments in the format given in the Sample Run (hint: use the __str__() method implicitly)

    '''

    

def save_scheduled_appointments():#Gordon
    '''
    1. Inputs appointment filename from user, checks if the file already exists and if so, allows user to proceed (i.e. overwrite the file) or repeat the filename input
    2. Iterates over each appointment in the list and if scheduled (i.e. appt_type != 0), writes the appointment to the file in the proper CSV format (hint: use the format_record() method)
    3. Returns the number of scheduled appointments saved

    '''
    saveFile = input("Would you like to save all scheduled appointments to a file (Y/N)?")
    if saveFile.upper() == "Y":
        fileName = input("Enter appointment filename: ")
        import os
        rec=0
        if os.path.exists(fileName):
            confirm = input("File already exists. Do you want to overite it (Y/N)?")
            if confirm.upper() =="Y":
                f= open(fileName,"w")
                for day in week:
                    for time in range (9,17):
                        if appt_list[day][time]!='':
                            f.write(appt_list[day][time].format_record())
                            rec+=1
                f.close()
                print(f"{rec} scheduled appointments have been successfully saved")
            else:
                fileName = input("Enter appointment filename: ")
                f=open(fileName,'w')
                for day in week:
                    for time in range (9,17):
                        if appt_list[day][time]!='':
                            f.write(appt_list[day][time].format_record())
                            rec+=1
                f.close()
                print(f"{rec} scheduled appointments have been successfully saved")
        else:
            f = open(fileName,"w")
            for day in week:
                for time in range (9,17):
                    if appt_list[day][time]!='':
                        f.write(appt_list[day][time].format_record())
                        rec +=1
            f.close()
            print(f"{rec} scheduled appointments have been successfully saved")
    # for day in week: 
    #     for book in appt_list[day].values():
    #         if book:
    #             print (book)

def cancel_appointment(): #Nam
    pass

def schedule_appointment(): #Gordon
    print ("** Schedule an appintment **")
    day_of_week = input("What day: ")
    start_time_hour = int(input("Enter start hour (24 hour clock): "))
    while appt_list[day_of_week][start_time_hour]!='':
        print ("Sorry, the time slot is not available, please re-enter")
        start_time_hour = int(input("Enter start hour (24 hour clock): "))
    else:
        client_name = input("Client Name: ")
        client_phone = input("Client Phone: ")
        appt_type = int(input("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120\nType of Appointment: "))
        appt_list[day_of_week][start_time_hour] = ap.Appointment(day_of_week,start_time_hour)
        appt_list[day_of_week][start_time_hour].schedule(client_name,client_phone,appt_type)
        print (f"OK, {client_name}'s appointment is scheduled")
        

def main(): #Gordon
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
    print ("Starting the Appointment Manager System")
    create_weekly_calendar()
    load_scheduled_appointments()
    print_menu()
    while userchoice not in [1,2,3,4,9]:
        print ("Sorry that is not a valid appointment type!")
        print_menu()
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
                print ("** Exit the system **")
                save_scheduled_appointments()
                exit()

if __name__ =="__main__":
    main()

    