#H e l l o W o r l d !
#0 1 2 3 4 5 6 7 8 9 10 11
#Index from 0 to 11 count

String = "Hello"
print(String[0]) #H
print(String[1]) #E
print(String[2]) #L
print(String[3]) #L
print(String[4]) #O

original_string = "Hello world!"
new_sting = original_string[0:5] #slicing the string
print(new_sting)

# \n - newline
# \t - tab

print("Hello \n\"bob\"")

print("The escape sequence \\n creates a new line in a print statement")
# Output: The escape sequence \n creates a new line in a print statement

# format .format()
name = "Peter"
print("Hello, {}!".format(name))

name = "Peter"
print(f"Hello, {name}!")

number_builder = ""
i = 0

while i <= 50:
    if i % 2 == 0:
        number_builder += str(i) + " "
    i += 1
print(number_builder)

number_builder = [] #the variable should be a list rather then a string
i = 0

while i <= 50:
    if i % 2 == 0:
        number_builder. append(str(i))
    i += 1
print(" ".join(number_builder))


#Task

string = "I am coding"
result = "" #building up a new string
for idx in range(len(string)):
    if not idx % 2:
        result = result + string[idx].upper() #using upper, lower loop
    else:
        result = result +string[idx].lower()
print(result) #printing the result

string =result.split() #using the same string
new_result = ""
for i in range(len(string)):
    if i % 2 == 0:
        new_result += string[idx].upper()
    else:
        new_result += string[idx].lower()

print(new_result)
