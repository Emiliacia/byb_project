# =============  Writing if statements ==================
# if statements are a type of control structure which control the flow of logic within a program.
# if statements contain a condition.
# Conditions are statements that can only evaluate to a boolean value, True or False.
# If the condition is True then the indented statements are executed; if the condition is False then the indented statements are skipped.
# In Python, if statements have the following general syntax:
#               if condition :
#                       indented statements
# Examples
#age = 20
#if age >= 18:
       # print("You're over 18 and can come in.")


# Explanation:

# If they are not 18 or older, then the print statement is skipped and nothing is printed.
# As it stands this code will always produce the same output. We could change it to accept 
# input from a user to set the age, which would result in a more dynamic and useful program
#Task 1

#Asking for age input.


#Converting age into an integer.
age = int(user_input)
print(age)
# We check if the age is greater than 101.
# If the age is greater, than 100 print out "Sorry you're dead."
if age > 101:
        print("Sorry you're dead.")   
# If the age is greater, than 40 print out "You're over the hill."
elif age >= 40:
        print("You're over the hill.")     
# If the age is greater, than 65 print out "Enjoy the retirenment."
elif age >= 65:
        print("Enjoy the retirement.")
# If the age is less, than 13 print out "You qualify for the kiddie discount." 
elif age < 13:
        print("You qualify for the kiddie discount.")
 # If the age is equal, to 21 print out "Congrats on your 21st!"
elif age == 21:
        print("Congrats on your 21st!")
  # If the age is more than 14 but less than 39 print out "Age is but a number.")     
elif 14 <= age <= 39:  
         print("Age is but a number.")