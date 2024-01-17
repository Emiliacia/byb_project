# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #missing parentheses
print ("\n")


# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # indentantion removed, changed  to lowercase, removed extra '=', removed invalid integer
age = int(age_Str) # indentantion removed
print("I'm" , age , "years old.") # indentantion removed


# Variables declaring additional years and printing the total years of age
years_from_now = "3" # indentantion removed
total_years = age + int(years_from_now) # indentantion removed, added int to variable
print ("The total number of years:", total_years) #undefined variable

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months =(total_years * 12 ) + 6 #added years to total as it was undefined
print ("In 6 months, I'll be " , total_months, " months old")

#HINT, 330 months is the correct answer