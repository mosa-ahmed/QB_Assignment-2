import math
from multipledispatch import dispatch

# 1- Design a class named Person and its two subclasses named Student and Employee
class Person:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def Print_data(self):
        print(Person.__name__, '->', f"Name: {self.name} \n \t  Address: {self.address}  \n \t  Phone number: {self.phone_number} \n \t  Email: {self.email}")


class Student(Person):

    class_statuses = ['freshman','sophomore','junior','senior']

    def __init__(self, name, address, phone_number, email, class_status):
        super().__init__(name, address, phone_number, email)
        if class_status.lower() in self.class_statuses:
            self.class_status = class_status.lower()
        else:
            raise ValueError("Invalid class status")
        
    def Print_data(self):
        print(Student.__name__, '->', f"Name: {self.name} \n \t  Address: {self.address}  \n \t  Phone number: {self.phone_number} \n \t  Email: {self.email} \n \t  Class Status: {self.class_status}")


class Employee(Person):
    def __init__(self, name, address, phone_number, email, office, salary):
        super().__init__(name, address, phone_number, email)
        self.office = office
        self.salary = salary

    def Print_data(self):
        print(Employee.__name__, '->', f"Name: {self.name} \n \t  Address: {self.address}  \n \t  Phone number: {self.phone_number} \n \t  Email: {self.email} \n \t  Office: {self.office} \n \t  Salary: {self.salary}")


class Faculty(Employee):
    def __init__(self, name, address, phone_number, email, office, salary, office_hours, rank):
        super().__init__(name, address, phone_number, email, office, salary)
        self.office_hours = office_hours
        self.rank = rank

    def Print_data(self):
        print(Faculty.__name__, '->', f"Name: {self.name} \n \t  Address: {self.address}  \n \t  Phone number: {self.phone_number} \n \t  Email: {self.email} \n \t  Office: {self.office} \n \t  Salary: {self.salary} \n \t  Office Hours: {self.office_hours} \n \t  Rank: {self.rank}")


class Staff(Employee):
    def __init__(self, name, address, phone_number, email, office, salary, title):
        super().__init__(name, address, phone_number, email, office, salary)
        self.title = title

    def Print_data(self):
        print(Staff.__name__, '->', f"Name: {self.name} \n \t  Address: {self.address}  \n \t  Phone number: {self.phone_number} \n \t  Email: {self.email} \n \t  Office: {self.office} \n \t  Salary: {self.salary} \n \t  Title: {self.title}")

#=================================================================================================

# 2- Design a class named MyInteger
class MyInteger:
    value = 0
    def __init__(self, value):
        self.value = value
    
    def isEven(self):
        if self.value % 2 == 0:
            return True
        else:
            return False
        
    def IsOdd(self):
        if self.value % 2 != 0:
            return True
        else:
            return False
        
    def IsPrime(self):
        if self.value <= 1:
            return False
        if self.value == 2:
            return True
        if self.value % 2 == 0:
            return False
        
        max_divisor = math.isqrt(self.value) + 1
        for i in range(3, max_divisor, 2):
            if self.value % i == 0:
                return False
        return True    
        
    @dispatch(int)
    def isEven(value):
        if value % 2 == 0:
            return True
        else:
            return False
        
    @dispatch(int)
    def IsOdd(value):
        if value % 2 != 0:
            return True
        else:
            return False    
        
    @dispatch(int)
    def IsPrime(value):
        if value <= 1:
            return False
        if value == 2:
            return True
        if value % 2 == 0:
            return False
        
        max_divisor = math.isqrt(value) + 1
        for i in range(3, max_divisor, 2):
            if value % i == 0:
                return False
        return True    
    

