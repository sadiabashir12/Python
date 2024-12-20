num_char = len (input ("what is your name ?"))
#print ("your name has" + name + "characters") #can only concatinate string to string and not string to interger

#type() => tells us about the type of data in the parentheses
print (type(num_char))

#In type_casting we change data from one data_type to another
#now we convert the integer type of data to sting type
new_num_char = str(num_char)
print ("Your name has " + new_num_char + " characters")

print ("The sum is = " , 90 + float(90.8))

print ("The letter present at it index 3 is :" ,"hello"[3])