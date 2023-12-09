
'''

# PART 2

File Name: appt_manager

'''

import appointment as apt
import csv
from pathlib import Path


'''
Function Name: create_weekly_calender
Parameters: none
Returns: list of appointments
Description: Creates a list of appointments. This list serves as a template for the appointments for Days (Mon - Sat)
             and the hours from 9 to 16  (24) Hour Format.
             The calender is used for saving appointments which are read from csv file. 

'''


def create_weekly_calender():
    calendar = []
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    available_hours = ["09", "10", "11", "12", "13", "14", "15", "16"]

    for day in days_of_the_week:
        for hour in available_hours:
            obj = apt.appointment(day, hour)
            calendar.append(obj)

    return calendar

'''
Function Name: print_menu
Parameters: calender
Returns: none
Description: The function prints menu to prompt the user to select any option.
'''


def print_menu(calender):

    while True:

        print("Jojo\'s Hair Salon Appointment Manager")
        print("======================================")
        print("1) Schedule an appointment")
        print("2) Find appointment by name")
        print("3) Print calendar for a specific day")
        print("4) Cancel an appointment")
        print("9) Exit the system")
        choice = int(input("Enter Your Selection: "))

        if 1 <= choice <= 4 or choice == 9:

            if choice == 1:
                schedule()

            elif choice == 2:
                show_appointments_by_name()

            elif choice == 3:
                print_calender(calender)

            elif choice == 4:
                cancel_appointment(calender)

            elif choice == 9:
                return None

        else:
            print("Invalid choice. Please enter a number between 1 (Inclusive) and 4 (Inclusive) or 9 to exit.")
            choice = int(input("Enter Your Selection: "))


'''
Function Name: cancel_appointment
Parameters: calender
Returns: None
Description: Cancels any appointment. Prompts the user to enter day and time. Appointment is searched via find_appointment_by_time function
             When the appointment is found, the cancel function of the appointment class is invoked 
'''


def cancel_appointment(calender):

    print("** Cancel an appointment **")
    day = input("What day: ")
    hour = input("Enter start hour (24 hour clock): ")
    appt = find_appointment_by_time(calender, day, hour)

    if appt:
        print(f"{day}, {hour}, - , {appt.get_end_time_hour()}, for , {appt.get_client_name()}, has been cancelled!")
        appt.cancel()

    else:
        print("Appointment Not Found")


'''

Function Name: find_appointment_by_time
Parameters: Calender, day, time
Returns: A single appointment or none
Description: Finds a single appointment in the calender via searching by day and time

'''


def find_appointment_by_time(calender, day, start_hour):
    for appointment in calender:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour:
            return appointment

    return None


'''

Function Name: load_scheduled_appointments
Parameters: calender
Returns: count(integer) of how many appointments have been loaded
Description: Reads the csv file and loads the appointments in the calender

'''


def load_scheduled_appointments(calender):

    while True:
        file_choice = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").upper()

        if file_choice == 'Y':
            file_name = input("Enter Appointment filename: ")
            path = Path(file_name)

            if path.exists():
                break
            else:
                print("File Not Found, Re-enter the appointment filename: ")
        elif file_choice == 'N':
            print("Not Loading From a File (New Appointments Will be created)")
            return 0
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

    counter = 0
    with open(file_name, 'r') as file:
        read_obj = csv.reader(file)

        for row in read_obj:
            counter += 1

    '''
    
    PLEASE WRITE THE CODE TO READ THE CSV FILE AND SCHEDULE APPOINTMENTS IN THE CALENDER
    
    '''
    return counter


def show_appointments_by_name():
    print("Implementation Remaining...")


def schedule():
    print("Implementation Remaining...")


'''
Function Name: print_calender
Parameters: Calender
Returns: None
Description: Prints the appointment calender

'''


def print_calender(calender):
    day = input("Enter day of week: ")
    print(f"Appointments for {day}")

    print(f"Client Name".ljust(20), "Phone".ljust(20), "Date".ljust(20), "Start".ljust(20), "End".ljust(20), "Type")
    print("-".ljust(120, "-"))

    for appointments in calender:
        if appointments.get_day_of_week() == day:
            print(appointments.get_client_name().ljust(20), appointments.get_client_phone().ljust(20), appointments.get_end_time_hour(), "          ", appointments.get_appt_type())

    return


def main():
    print("Starting the Appointment Manager System")

    calender = create_weekly_calender()

    print("Weekly Calender Created")

    counter = load_scheduled_appointments(calender)
    print(f"{counter}  previously scheduled appointments have been loaded")

    if counter != 0:
        print_menu(calender)


if __name__ == "__main__":
    main();
