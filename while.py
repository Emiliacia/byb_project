#Using loop strategy, statting from 0
sum1 = 0
#Initial even integer for the sum
i = 2
while sum1 <=250:
   sum1 +=i
#Update statement, shorthand for i = i + 2
   i += 2
   print(sum1)

#Example2
i = 0
while i < 10:
   i += 1
   print(i)

#Example3
my_number = 0
while my_number < 100:
    my_number += 1
    if my_number == 23:
        break
    print(my_number)

#Example 4
my_number = 0
while my_number < 100:
    my_number += 1
    if my_number > 23:
        continue
    print(my_number)

#Task
number = 0
inputs =[]
#creating a program to continually ask the user to enter a number.
while True:
    number = int(input ("Enter a number: "))
    if number == -1:
        break
#The program will stop asking the user to enter a number if the user enters -1.       
#Calculating the averaga of the number inserted excluding -1 displaying the lengh with lens function.
    inputs.append(number)
    if len(inputs) > 0:
        average =sum(inputs)/len(inputs)
        print(f"Average{average}")
        print(f"Number of inputs:{len(inputs)}")
else:
    print("Missing inputs.")



