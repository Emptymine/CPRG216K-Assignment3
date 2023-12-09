
'''

# PART 1

Class Name: appointment

Attributes (Hidden): client_name                    string
                    client_phone                    string
                    appt_type (appointment type)    int
                    day_of_the_week                 string
                    start_time_hour                 string

Methods:
    Getter for every Attribute
    Setter for client_name, client_phone and appt_type
    appt_type_description
    end_time_hour
    schedule
    format_record
    string printing method

'''

class appointment:


    '''
    Constructor to initialize the variables
    It is made parameterized (As per requirements)
    '''

    def __init__(self, day_of_the_week, start_time_hour):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0
        self.day_of_the_week = day_of_the_week
        self.start_time_hour = start_time_hour


# GETTERS

    def get_client_name(self):
        return self.client_name

    def get_client_phone(self):
        return self.client_phone

    def get_appt_type(self):
        return self.appt_type

    def get_day_of_week(self):
        return self.day_of_the_week

    def get_start_time_hour(self):
        return self.start_time_hour


    def get_appt_type_desc(self):
        appt_type_dictionary = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return appt_type_dictionary.get(self.appt_type, "Appointment Number is wrong")


    def get_end_time_hour(self):
        return int(self.start_time_hour) + 1


# SETTERS
    def set_client_name(self, client_name):
        self.client_name = client_name

    def set_client_phone(self, client_phone):
        self.client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.appt_type = appt_type


    def schedule(self, client_name, client_phone, appt_type):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type


    def cancel(self):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0


    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_the_week},{self.start_time_hour:02}"


    def __str__(self):
        return f"{self.client_name} {self.client_phone} {self.day_of_the_week} {self.start_time_hour:02}:00 - {self.get_end_time_hour():02}:00 {self.get_appt_type_desc()}"
