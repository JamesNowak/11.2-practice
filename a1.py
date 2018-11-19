# this is the superclass
class Employee:
    def __init__(self, name, number):

        self.name = name
        self.number = number

    # this creates the mutators
    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

        # this creates the accessors
    def get_name(self):
        return self.name

    def get_number(self):
        return self.number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_rate):
        Employee.__init__(self, name, number)

        # initializes the exta attributes hourl_rate and shift_number
        self.shift_number = shift_number
        self.hourly_rate = hourly_rate
        # this creates the mutators

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

        # this creates the accessors
    def get_shift_number(self):
        return self.shift_number

    def get_hourly_rate(self):
        return self.hourly_rate
