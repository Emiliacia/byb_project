#Asking user to insert a sentence with input () function.
str_manip = input("Enter a sentence: " ) 
#Printing user input.
print(str_manip)
#Calculating and displaying the lenght with len() function.
print(len(str_manip))
#Unsure why counting more letters.
#Re-naming.
last_letter = str_manip[-1]
#Replacing last letter with @.
if len(str_manip) > 0:
    last_letter = str_manip[-1]
    print(last_letter)

    new_last_letter = str_manip[:-1] + "@"
#Priting the variable with replaced type.
    print(new_last_letter)

else:
    print("Enter a sentence.")
#Firstly we select the last 3 letters.
print(str_manip[-3:])
#Secondly we print the three last letter backwards # [start : end : step] Counting from 0
print(str_manip[-1:-4:-1])
#Printing the first 3 characters and the last 2 characters of the user input.
print(str_manip[0:3:])
print(str_manip[-2:])

#Creating a 5 letter word with the first 3 and last 2.
print(str_manip[0:4])

if len(str_manip) > 0:
    new_word = str_manip[0:3] + str_manip[-2:]
    print(new_word)
else:
    print("Invalid input.")





