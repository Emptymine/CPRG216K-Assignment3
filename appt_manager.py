import appointment

weekly_calendar = []

def create_weekly_calendar(): #Nam
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days_of_week:
        for hour in range(9, 17): #start_time_hour: 0900 to 1600
            weekly_calendar.append(appointment.Appointment(day, hour)) #pass "day" to "day_of_week" and pass "hour" to "start_time_hour"

def load_scheduled_appointments(): #Gordon
    # ???
    # ???
    # ???
    # print("File not found.")
    pass

def print_menu():
    print("Jojo's Hair Salon Appointment Manager")
    print("=====================================")
    print("1) Schedule an appointment")
    print("2) Find appointment by name")
    print("3) Print calendar for a specific day")
    print("4) Cancel an appointment")
    print("9) Exit the system")
    selection = input("Enter your selection: ")
    return selection


def find_appointment_by_time(): #Nam
    pass


def show_appointments_by_name(client_name): #Sam
    for appt in weekly_calendar:
        if client_name.lower() in appt.get_client_name().lower():
            print(appt)


def show_appointments_by_day(day): #Sam
    for appt in weekly_calendar:
        if appt.get_day_of_week().lower() == day.lower():
            print(appt)



def save_scheduled_appointments(): #Gordon
    # print("\n** Schedule an appointment **")
    # ??? = input("What day: ")
    # ??? = int(input("Enter start hour (24 hour clock): "))
    # ??? = input("Client Name: ")
    # ??? = input("Client Phone: ")
    # print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
    # ??? = int(input("Type of Appointment: "))

    # print("Sorry, that is not a valid appointment type!")
    # print("Sorry, that time slot is not available!")

    # print("OK, ??? appointment is scheduled!")
    pass

def cancel_appointment(): #?????
    pass

def main(): #Gordon
    create_weekly_calendar()
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    # ??? = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
        # ??? = input("Enter appointment filename: ")
        # ??? = print("File not found.")
        # ??? = input("Re-enter appointment filename: ")
        # ??? = print("???? previously scheduled appointments have been loaded")
    
    userSelection = print_menu()    # pass selection into userSelection
    if userSelection == "1":
        save_scheduled_appointments()
    elif userSelection == '2':
        client_name = input("Enter Client Name: ")
        show_appointments_by_name(client_name)
    elif userSelection == '3':
        day = input("Enter day of week: ")
        show_appointments_by_day(day)
    elif userSelection == '4':
        cancel_appointment()    
    elif userSelection == '9':
        input("Would you like to save all scheduled appointments to a file (Y/N)? ").lower()
        # ??? = input("Enter appointment filename: ")
        # ???
        # ???
        print("Good Bye!")
        

if __name__ == "__main__":
    main()

