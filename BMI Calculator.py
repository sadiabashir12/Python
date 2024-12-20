#BMI CALCULATOR
#Enter weight in kilograms
weight = int (input("Eneter your weight in kg : "))
#Enter height in meters
height = float (input("Enetr uour height in meters : "))
#Calculating Body Mass Index (BMI)
bmi = weight/(height**2)
print ("Your BMI is : ",bmi)

if bmi < 18.5 :
   print ("Underweight")
if bmi > 18.5 and bmi < 25 :
   print ("Normal")
if bmi > 25 and bmi < 30 :
   print ("Overweight") 
if bmi > 30 :
   print ("Obese")