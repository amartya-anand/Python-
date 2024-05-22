# map()

a = [2,5,10,1,3] 

b = map(lambda x:x**2,a) 

print(b) 
print(list(b)) 

 
def add_tuples(t): 

    return sum(t) 

tup_list = [(1,2,3),(1,1,1),(2,1,2)] 
sum_list = map(add_tuples,tup_list) 

print(list(sum_list)) 

names = ['apple','mango','grapes','cherry'] 
 
def make_upper(s): 

    return s.upper() 

name_up = map(make_upper,names) 

print(list(name_up))  

# Filter()

num_set = {1,2,5,4,8,11,35,28} 

def even_num(num): 

    if num%2 == 0: 

        return(num) 

evens = filter(even_num,num_set) 

print(list(evens)) 

# Reduce - Returns a single value

from functools import reduce 

my_list=[1,2,3,4,5,6,7,8,9,10] 

summed = reduce(lambda x,y:x+y,my_list) 

print(summed) 

# To identify the object type

var1 = 'hello' 
check1 = isinstance(var1,str) 

print(f'var1 is string?: {check1}') 

check2 = isinstance(var1,int) 
print(f'var1 is integer?: {check2}') 

# check the tuple datatype 

var2 = (1,2,3,4,5) 
check2 = isinstance(var2,tuple) 

print(f'var2 is tuple?: {check2}') 

# check the list datatype 

var3 = [1,2,3,4,5] 
check3 = isinstance(var3,list) 

print(f'var3 is list?: {check3}') 

# check the dict datatype 

var4 = {'one':1,'two':2,'three':3,'four':4} 
check4 = isinstance(var4,dict) 

print(f'var4 is dict?: {check4}') 
 