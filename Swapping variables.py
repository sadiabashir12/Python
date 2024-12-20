#Swapping variables
#Method 1 
a = input ("a")
b = input ("b")
#We temporarily store the value of "a" in a variable "temp"
temp = a 
a = b
b = temp
print ("after swapping values , the value of a is : " + a)
print ("after swapping values , the value of b is : " + b)

#Method 2 
a = input ("a ")
b = input("b ")
a, b = b, a 
print ("a = " , a)
print ("b = " , b)
