
#Age calculation with birth year.

from datetime import date
dob =  input("Enter your date of birth year: ")
today = date.today()
cruntYear = today.strftime("%Y")
age =  int(cruntYear) - int(dob)
print(age)


#The area calculation of a rectangle using length and width variables calculation
length = 50
width = 100
area = length * width
print("rectangle:", area) 

#the area of calculation a circle.

radious = 50   
area = 3.14 * radious * radious  
print("circle:", area) 

#The area calculates of the cube.
side = 50
area = 6 * side * side  
print("cube:", area)  


#Fahrenheit to Celsius calculation.
fahrenheit = 100
celsius = (fahrenheit - 32) * 5/9  
print("Celsius:", celsius) 

#Given number of seconds into minutes and seconds using variables.
seconds = 1000
minutes = seconds // 60
remSeconds = seconds % 60  
print("Minutes:", minutes, "Seconds:", remSeconds)

#The calculation o percentage.
total_marks = 100
obtained_marks = 80
percentage = (obtained_marks / total_marks) * 100
print("Percentage:", percentage)

