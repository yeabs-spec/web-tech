class student:   #creating class
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'selam {self.name}'

    def greet(self):
        return f'hello {self.name}'

stu_obj = student('hanna') #creating object
print(stu_obj.greet())
print(stu_obj.__str__())


class passenger:
    def __init__(self,name,passport_no): # creating constructor
        self.name = name
        self.passport_no = passport_no
    def __str__(self):
        return self.name

class flight:
    def __init__(self):
        self.destination
        self.departure
        self.passenger = []
        self.capacity

    def add_passenger(self,name,passport_num):
        obj = passengers(name,passport_num)
        if self.capacity <= self.passenger.count():
            return f'the flight is full'
        
        else:
            self.passenger.append(obj)
            return f'you have sucessfully booked your flight'

