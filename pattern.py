#Practicing the for loop
#Before runing the loop you need a sequence which is a list or a string(my_list)
my_list = [2, 4, 6, 8, 10]
for index_variable in my_list:
    print(index_variable)
#Notice the indentention and the colon. 
#The range(start index:end index) which means the start is included and the end is excluded.
#If you want to print your list (my_list) and if u want separate number on each line you need to use (index_variable)

#In for the loop the variable i (which is an integer)
#is the range of 1 to 10(1,2,3,4,5,6,7,8,9)
for i in range(1,10):
    print(i)
#The range (1,10) specifies that i = 1 in the first
#interation of the loop, so 1 will be printed in the first interation of the code
#then the code will run again this time i = 2, and 2 
#will be printed out, etc., until i =10
#At this point, i is no longer in the range (1,10) so the code will stop executing.
#The code intendented is repeated.

#THE USE OF IF STATEMENT WITH FOR LOOP:
for i in range (1,10):
    if i > 5:
        print(i)

#RULES:
#Initialise loop: the loop needs to use a variable as its counter variable, to tell the computer how many time to execute the loop
#Loop test: is a boolean expression that evaluates if is True or False and is evaluated before any iteration. If is True contrl passes to the loop body, if is False passes to the first statement after the loop body.
#Update statement:assign new values to the loop control variables, typically ises the increment i+=1 and happens after the body has been executed

#BREAK STATEMENT, causes an immediate exit from the loop to the first statement after the loop body

num_list =[1, 2, 3, 4, 5]
found = False
num = int(input("Input a number from 1 to 10 and find out if it's in our list: "))
if num<1 or num>10:
    print("Number out of range")
else:
    for number in num_list:
        if num == number:
                found = True
                break
    print(f'List contains {num}:{found}')

#NESTED LOOPS
for x in range(1, 6):
     for y in range(1, 6):
         print(f"{x} * {y} = {x*y}")
         print("")

#TASK
#requested pattern
pattern ="*"
#for loop function
for num in range (1, 6):
    to_print = pattern* num
    print(to_print)
#using if function for when reaching 5 to go down
    if num == 5:
        count_down = 5 - num
        to_print = pattern* count_down
print(to_print)
#having troubles 
