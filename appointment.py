class Appointment:
    def __init__(self,client_name, client_phone, appt_type, day_of_week, start_time_hour):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour
    
    def Getter_client_name(self):
        return self.client_name
    
    def Getter_client_phone(self):
        return self.client_phone
    
    def Getter_appt_type(self):
        return self.appt_type
    
    def Getter_day_of_week(self):
        return self.day_of_week
    
    def Getter_start_time_hour(self):
        return self.start_time_hour
    
    def get_appt_type_desc(self):
        '''•	An additional “getter” method that translates and returns the object’s appt_type as a text description, I.e.:
        appt_type    description
        0                   Available
        1                   Mens Cut
        2                   Ladies Cut
        3                   Mens Colouring
        4                   Ladies Colouring
        '''
        