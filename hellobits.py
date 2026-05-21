print("Hello Anaadi")

age = int( input("Whats your age? ") )
n = 10 + age
print("value of n is ", n)
is_adult = age >= 18 # relational operator
# print( type(is_adult) )
print( "is_adult",is_adult )
print("not is_adult", not is_adult )

# we check if user is an adult or not
if age == 18: # `logical operator or , not 
        print("You are a teenager")     

if not is_adult:
    print("You are not an adult")
else:
    print("You are no one")    
# print("End of program")

# -block True- if -condition- else -block False-  
print("You are an adult") if is_adult else print("You are not an adult")