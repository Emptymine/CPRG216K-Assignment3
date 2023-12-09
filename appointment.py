class Appointment:
    
    #Constructor:
    def __init__(self, day_of_week, start_time_hour):
        self.client_name = ""   
        self.client_phone = ""  
        self.appt_type = 0      
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour

    #Getters:
    def get_client_name(self):
        return self.client_name
    
    def get_client_phone(self):
        return self.client_phone
    
    def get_appt_type(self):
        return self.appt_type
    
    def get_day_of_week(self):
        return self.day_of_week
    
    def get_start_time_hour(self):
        return self.start_time_hour
    
    #additional “getter” method that translates and returns the object’s appt_type as a text description
    def get_appt_type_desc(self):
        appt_types = {0: "Available", 1: "Mens Cut", 2: "Ladies Cut", 3: "Mens Colouring", 4: "Ladies Colouring"}
        return appt_types.get(self.appt_type, "Sorry that is not a valid appointment type!")

    #additional “getter” method that returns the value of the object’s start_time_hour + 1
    def get_end_time_hour(self):
        return self.start_time_hour + 1

    # Setters:
    def set_client_name(self, client_name):
        self.client_name = client_name

    def set_client_phone(self, client_phone):
        self.client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.appt_type = appt_type

    #schedule appointment
    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    #cancel appointment
    def cancel(self):
        self.set_client_name("")
        self.set_client_phone("")
        self.set_appt_type(0)

    #return CSV string representation
    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour}"

    #return string representation of the appointment object
    def __str__(self):
        return f"{self.client_name:20s}{self.client_phone:15s}{self.day_of_week:10s}{self.start_time_hour:>2}:00  - {self.get_end_time_hour()}:00 {self.get_appt_type_desc():^20}"