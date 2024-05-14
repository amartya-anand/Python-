def display_days(): 

    days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 

    for day in days_list: 

        print(day) 


# function call 

display_days() 

def greet(): 

    print(f"Good Morning, {username} !") 


# get username from user 

username = input("Enter User Name:") 

# function call 

greet() 

# Factorial

def facto(x): 

    if x==0: 

        return 1 

    else: 

        return(x*facto(x-1)) 

# lets calculate factorial of 4 

four_fact=facto(4) 

print(four_fact) 

# lets calculate factorial of 3 

three_fact=facto(3) 

print(three_fact) 

num = int(input("Enter a number: ")) 

factorial = 1 

if num < 0: 

    print(" Factorial does not exist for negative numbers") 

elif num == 0: 

    print("The factorial of 0 is 1") 

else: 

    for i in range(1,num + 1): 

        factorial = factorial*i 

    print("The factorial of",num,"is",factorial) 

def two_nums_add(): 

    # calculate addition 

    addition=num1+num2 

    # return the addition 

    return(addition) 

# lets define two variables 

num1=10 

num2=20 

# function call and store the sum in result variable 

result=two_nums_add() 

print(f"Their addition(num1+num2): {result}")     