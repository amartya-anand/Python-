# Anonymous Function

greet=lambda x:print(x) 

greet('Hello') 

addn = lambda x,y:print(x+y) 

addn(5,6) 

# Positional arguments
addn_prod = lambda x,y:(x+y,x*y) 
addn,prod = addn_prod(10,10) 

print(addn) 
print(prod) 

# Function value stored in a variable

def fav_subject(sub): 
    return sub 

s = fav_subject 

print(s("Mathematics")) 
print(fav_subject("Mathematics")) 

# Function passed as an argument to another function

def favBook(): 
    return "Mrityunjoy" 

def favourite(func): 
    print(func()) 

favourite(favBook) 

# Function returned from another function

def favBook(x): 

   def favWriter(y): 

       return x+"," +y 

   return favWriter 

# Save outer function inside variable 

book = favBook("Mrityunijoy") 

print(book("Shivaji Savant"))
