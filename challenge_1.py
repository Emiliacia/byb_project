#Asking the user to enter the lenghts of all three sides of a triangle.
import math
side_1 = float(input("Insert the lenght of the first side of the triangle: "))
side_2 = float(input("Insert the lenght of the second side of the triangle: "))
side_3 = float(input("Insert the lenght of the third side of the triangle: "))
#Checking if is valid
if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
#Calculating the area of the triangle
    s = (side_1 + side_2 + side_3)/2
    area = math.sqrt(s*(s- side_1)*(s- side_2)*(s- side_3))
    print(f"The area of the triangle is: {area}")
else:
    print("The given side lenghts do not form a triangle.")



