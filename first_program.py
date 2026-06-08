#Print Hello World
print("Hello World")

#Create a variable to store my name
first_name = "Nathaniel"

#Create a variable for the last name
last_name = "Bian"

#Write a python statement to display "My full name is Nathaniel Bian"
print("My full name is", first_name, last_name, sep="")

#Print using the f string (string interpolation)
print(f"My full name is {first_name} {last_name}")

#Create variables to store age and weight
age = 15
weight = 153.6
half_age = age / 2

#Print a sentence with name, age, and weight
print(f"My name is {first_name} {last_name}\nI am {age} years old and I weigh {weight} lbs")

#Get and print the data type for age, weight, and half_age
print("\nChecking Data Types\n-------------------")
print(type(age))
print(type(weight))
print(type(half_age))

#Write 3 statements using string interpolation (f string) to print descriptive sentences for the data types
print(f"Variable age is an {type(age)}")
print(f"Variable weight is a {type(weight)}")
print(f"Variable half_age is a {type(half_age)}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")
