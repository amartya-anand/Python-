print("Hello World!")

x = 4
y = 6
print(x)

print(type(4))
print(type("Hello World"))
print(type(3.4))
print(type("3.4"))
print(type("4"))

# This is an example of Semantic error

print(1,000,000)

# Following are the ways in which a variable name given legally in Python

variable_decleration = 123
another_way = 321
One_more = 456

print(variable_decleration)
print(another_way)
print(One_more)

# Various operators in Python
# Exponent
a = 2**3
print(a)

# Modulus operator - Gives us the remainder of division
b = 7 % 3
print(b)

# Division operation - Gives the Quotient in Floating point
c = 7 / 3
print(c)

# Division operation - Gives the Quotient in Integer,also known as floor division
d = 7 // 3
print(d)

# While evaluating expression,Python follows PEMDAS convention
print(3**2+1)
print(3*2/2+2)

# String Operations
first = 10
second = 20
print(first+second)
third = "10"
fourth = "20"
print(third+fourth)
fifth = "Ram\n"
sixth = 6
print(fifth*sixth)

# Asking for user input
#name = input("Who are you\n")
#print("Hello" +name)

# Boolean
print(5 == 5)
print(5 == a)
print(type(True))

# Comparison Operators
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x is y)
print(x is not y)

# Logical Operators
print (x > 0 and y < 10)
print (x > 10 or y > 5)
print (not(x<y))

# Conditional Statements

if x > 0:
    print("X is positive")

# Here pass works as placeholder and does nothing

if x > 0:
    pass   

if x % 2 == 0:
    print("X is even")
else:
    print("X is odd number")    

# Chained conditionals

if x < y:
    print("X is less than y")
elif x > y:
    print("X is more than y")
elif x == y :
    print("X and y are equal")
       
# Nested conditionals

if x == y:
    print("X is equal to y")
else:
    if x < y:
        print("X is less than y")
    else:
        print("X is greater than y") 

# Try-Catch block

#temp = input("Enter the temperaure in Fahrenheit:")
#try:
    #temp_fahr = float(temp)
   # cels = (temp_fahr - 32.0) * 5.0 / 9.0
    #print(cels)
#except:
   # print("Please enter the number")     


# Data type

first_name = "Amartya"
last_name = "Anand"
roll_no = "980"
print(first_name + " " + last_name) 

# String Formatting

Full_name = 'Hello {} {}, Welcome back'.format(first_name,last_name)
print(Full_name)

# Slicing of String => [start:end:step]
my_address = "Kumar Pebble Park"
print(my_address[0])
print(my_address[:])
print(my_address[0:7])
print(my_address[11:])
print(my_address[3:10])
print(my_address[-1]) #Last character of string
print(my_address[-9:])
print(my_address[-15:-9])
my_phone_number = "123456789"
print(my_phone_number[::2]) # Works only for string
print(my_phone_number[::3]) 
print(my_phone_number[:6:2])
print(my_phone_number[2:9:2])

# String methods

String_methods = "aMaRtYa"
print(len(String_methods))
print(String_methods.upper())
print(String_methods.lower())
print(String_methods.capitalize())
print(String_methods.islower())
print(String_methods.isupper())
print(String_methods.replace("M","m"))
print(String_methods.split())

# List => Mutable

fruit_bastket = ['Apple','Banana','Mango']
mixed_basket = ['Potato',123,'Onion',543]
nested_list = [['10kg',1,"A"],['B',2,'20kg']]

print("The value of the list is:",fruit_bastket)
print(fruit_bastket[:])
print(fruit_bastket[0])
print(fruit_bastket[3:])
print(fruit_bastket[2:5])
print(fruit_bastket[-1])
print(fruit_bastket[-3:])
print(fruit_bastket[-4:-1])
print(fruit_bastket[::-1]) # Reversing the list

# List Methods

print(len(fruit_bastket))
print(len(mixed_basket))
print(len(nested_list))
mixed_basket.insert(2,'Watermelon')
print(mixed_basket)
mixed_basket.append("Orange")
print(mixed_basket)
fruit_bastket.extend(nested_list)
print(fruit_bastket)
fruit_bastket.remove('Banana')
print(fruit_bastket)
fruit_bastket.pop()
print(fruit_bastket)

# Tuple => Immutable

season = ('Summer','Rainy','Winter')
print(season)

# Dictionary => Key:Value

roll_no = { 1 : 'Amartya', 2 : 'Anand' }
print(type(roll_no))
print(roll_no)
print(roll_no[2])
roll_no[3] = 'Aniket'
print(roll_no)

# Dictionary methods

print(roll_no.keys())
print(roll_no.values())
print(roll_no.items())

# Nested Dictionary

society = {
    'wing_A' : {'flats' : 20, 'vehicles' : 22},
    'wing_D' : {'flats' : 21, 'vehicles' : 32},
    'wing_C' : {'flats' : 30, 'vehicles' : 42},
    'wing_B' : {'flats' : 26, 'vehicles' : 52},
}
print(society['wing_B']['flats'])

# Dictionary Comprehension

num = { 'one' : 1, 'two' : 2, 'three' : 3}
squared_num = {k: v**2 for (k,v) in num.items()}
print(squared_num)

# Set => Unordered

my_set = { 1,2,"a"}
print(my_set)
my_set2 = { 3,4,"b"}
print(my_set.union(my_set2))

# Typecasting

num = 100
print(type(num))
num2 = str(num)
print(type(num2))

n = "123"
name2 = int(n)
print(type(n))
print(type(name2))

t = [1,2,3]
print(type(t))
x = tuple(t)
print(type(x))

tup1 = ('a','b','c')
print(type(tup1))
list1 = list(tup1)
print(type(list1))



