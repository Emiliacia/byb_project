
username = (input)("Enter username.")
if not username:
    print("Username ivalid. Please add valid username.")
#Lower/upper case
name = "Iron man Captain America"
splitName =name.split(" ")
print(splitName)
temp =""
for i in range(len(splitName)):
    if i % 2 == 0:
        temp+=splitName[i].upper() +" "
    else:
        temp+=splitName[i].lower() +" "
print(temp)

sample_data = {}
"Name": ["Alice","Bob","Charlie","Davic","Eve"]
"Age" : [25, 30, 35, 39, 22]
print(sample_data.items())
for key,value in sample_data.items():
    print(f"{name} -{value}")
