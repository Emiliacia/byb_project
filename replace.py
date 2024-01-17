'''

I am completing task 1 which requires to use the replace function.

'''

string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(string)
new_string = string.replace("!"," ")
print(new_string)

'''
I am completing task 1 which requires to use the upper function.

'''
string = "The quick brown fox jumps over the lazy dog."
new_string = string.upper()
print(new_string)

'''
I am completing task 1 which requires to print the sentence in reverse.

'''
string = "The quick brown fox jumps over the lazy dog."
new_string = "The quick brown fox jumps over the lazy dog."[::-1]
print(new_string)





TASK
row_count = 5
start = 1
end = (2 * row_count) + 1

for row_number in range(start, end + 1):
    if row_number <= row_count:
        star_count = row_number
    else:
        star_count = end - row_number + 2
    
    if star_count != row_count + 1 and star_count != 0:
        for _ in range(star_count):
            print("*", end=" ")
        print()

# I cannot succeed 