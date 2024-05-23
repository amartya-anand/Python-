class Parent: 
    def func1(self): 
        print('this is a parent function') 

class Child(Parent): 
    def func2(self): 
        print('this is a child function') 

obj = Child() 

obj.func1() 

obj.func2() 

class Staff: 

    # class variable 

    raise_amount = 1.10 

    # constructor method 

    def __init__(self, first, last, pay): 

        self.first = first 

        self.last = last 

        self.pay = pay 

        self.email = first+'.'+last+'@school.com' 

 

    # method to display full name 

    def fullname(self): 

        return'{} {}'.format(self.first,self.last) 

 

    # method to hike pay by 30% 

    def apply_raise(self): 

        self.pay = int(self.pay*self.raise_amount) 

 

# Teacher is subclass 

class Teacher(Staff): 
    pass 

# Peon is subclass 

class Peon(Staff): 
    pass 

 

# Accountant is subclass 

class Accountant(Staff): 
    pass 

# BusDriver is subclass 

class BusDriver(Staff): 
    pass 

# lets create objects for different staffs 

# Teachers 

teacher1 = Teacher('Nilesh', 'Pande', 50000) 

teacher2 = Teacher('Rema', 'Singh', 45000) 

# Peons 

peon1 = Peon('Ram', 'Naik', 10000) 

peon2 = Peon('Ganesh', 'Patil', 10000) 

# Accountants 

acc1 = Accountant('Yash', 'Sharma', 20000) 

acc2 = Accountant('Yogesh', 'Shinde', 20000) 

# BusDrivers 

bus1 = BusDriver('Akash', 'Patil', 15000) 

bus2 = BusDriver('Dinesh', 'More', 15000) 

# Display the parent class properties 

print('Teacher Emails are:') 

print(teacher1.email) 

print(teacher2.email) 

print('-------------------') 

print('Peon Emails are:') 

print(peon1.email) 

print(peon2.email) 

print('-------------------') 

print('Accountant Emails are:') 

print(acc1.email) 

print(acc2.email) 

print('-------------------') 

print('BusDriver Emails are:') 

print(bus1.email) 

print(bus2.email) 

print('-------------------') 

# Staff is Super Class 

class Staff: 

    # class variable 

    raise_amount = 1.10 

    # constructor method 

    def __init__(self, first, last, pay): 

        self.first = first 

        self.last = last 

        self.pay = pay 

        self.email = first+'.'+last+'@school.com' 

    # method to display full name 

    def fullname(self): 

        return'{} {}'.format(self.first,self.last) 

    # method to hike pay by 30% 

    def apply_raise(self): 

        self.pay=int(self.pay*self.raise_amount) 


# Teacher is subclass 

class Teacher(Staff): 

    raise_amount = 1.15 
    pass 

# Peon is subclass 

class Peon(Staff): 

    raise_amount = 1.05 
    pass 

# Accountant is subclass 

class Accountant(Staff): 

    raise_amount = 1.20 
    pass 

# BusDriver is subclass 

class BusDriver(Staff): 

    pass 

# lets create objects for different staffs 

# Teacher 

teacher1 = Teacher('Nilesh', 'Pande', 50000) 

teacher1.apply_raise() 

# Peon 

peon1 = Peon('Ram', 'Naik', 10000) 
peon1.apply_raise() 

# Accountant 

acc1 = Accountant('Yash', 'Sharma', 20000) 
acc1.apply_raise() 

# BusDriver 

bus1 = BusDriver('Akash', 'Patil', 15000) 
bus1.apply_raise() 

# Display the increased salaries of staffs 

print('Staffs salaries after salary raise') 

print('Teacher Salary is:', teacher1.pay) 

print('Peon Salary is:', peon1.pay) 

print('Accountant Salary is:', acc1.pay) 

print('BusDriver Salary is:', bus1.pay) 

 



