#Add Two Numbers in Pyhton
#Author:cxy
#Using a function

#function to add two numbers
def add(a,b):
 #converting input to floatand adding
 result = float(a) + float(b)
 return result

#taking user input
a = input("First number: ")
b = input("Second number: ")

#calling function
res = add(a,b)
print("The Answer is: ")
print(res)
