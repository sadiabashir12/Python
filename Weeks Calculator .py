#calculaing weeks left in life
age = input ("enter your age : ")
years = 90 - int(age)
print (years)
#weaks left are
weaks = years * 52
#fstring is a formating string literal. By using this the expression inside the braces is replaced by value
print (f"you have {weaks} weaks left")
