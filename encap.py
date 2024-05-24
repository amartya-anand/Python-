class Hello: 

    def __init__(self,name): 

        # public variables 

        self.a=10 

        self._b=20 

 

    def public_method(self): 

        print('This is Public method') 

        print('Lets print public variables:') 

        # access public variables inside the class 

        print(self.a) 

        print(self._b) 

 

 

# class object 

hello = Hello('name') 

 

# access public variables 

print(hello.a) 

print(hello._b) 

 

# access public method 

hello.public_method()

class TechnoDexterous(): 

    def __init__(self): 

        self.course="Python Programming Course" 

        self.sections = ['Basics', 'Intermediate', 'Advanced'] 

        # private instance variable 

        self.__tech = "Python" 

 

    def course_name(self): 

        return f"Python Sections covered are: {self.sections}" 

 

# class object 

obj = TechnoDexterous() 

 

# access public class variable and method 

print(obj.course) 

print(obj.course_name()) 

# access private variable 

print(obj.__tech) 

# Getter Setter

class TechnoDexterous(): 

    def __init__(self): 

        print("Welcome to TechnoDexterous Platform !") 

        self.course = "Python Programming Course" 

        self.__tech = "Python" 

    def tech_name(self): 

        print(f"The technology is: {self.__tech}") 

    # getter method 

    def get_tech(self): 

        return self.__tech 

    # setter method 

    def set_tech(self,value): 

        self.__tech = value 

 

obj = TechnoDexterous() 

# lets call instance method to print tech name 

obj.tech_name() 

# set the value of private variable tech 

# using setter method 

obj.set_tech("Java") 

# lets get the private variable value using getter method 

print(obj.get_tech()) 

# Again call instance method check current tech name 

obj.tech_name() 

class Payment: 

    def __init__(self, price): 

        # private variable final_price 

        self.__final_price=price + price * 0.05 

    # getter method to get final_price 

    def get_final_price(self): 

        return self.__final_price 


book = Payment(10) 

# lets try to update __final_price 

book.__final_price = 0 

print(book.get_final_price()) 