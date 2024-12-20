#Tip and bill calculator 
print ("Welcome to the tip calculator")
bill = float (input ("What was the total bill ? $"))
tip = int (input ("How much tip would you like to give ? 10% , 12%  , 15% ? "))
people = int (input ("How many people to split the bill ? "))
#calculating the amount of tip
tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
#calculating total bill
total_bill = bill + total_tip
print ("Your total bill is : $", total_bill)
#calculating bill per person
bill_per_person = total_bill / people
#Now we round the bill to two decimal places
final_bill = round(bill_per_person , 2)
final_bill = "{:.2f}".format(bill_per_person)
print ("Each person should pay : $" , final_bill)