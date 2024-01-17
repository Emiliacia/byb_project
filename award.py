#Designing a program that determines the award a person competing in a triathlon will receive.
#The program will determine in minutes all thre events: swimming, cycling, and running.
#It will calculate and display the total time taken to comlete the triathlon.
#The reward a partecipant will receive is based on the total time taken to complete the triathlon.
# The qualifying time for a reward is 100 minutes.

#Dividing the triahlon in almost equal parts to make 100 minutes.

swimming = int(input("Enter the swimming completion time in minutes: "))
cyclying = int(input("Enter the cycling completion time in minutes: "))
running =int(input("Enter the running completion time in minutes: "))

completion_time = swimming + cyclying + running 

#Checking if qualified.
print(f"Swimming:{swimming} minutes")
print(f"Cycling:{cyclying} minutes")
print(f"Running:{running} minutes")

if completion_time <= 100:        # 'less than or equal to'
       print("You are within the qualifying time. Will be awarded Provincial Colours.")
elif completion_time <= 105:      # 'less than or equal to'
       print( "You are within the 5 minutes of the qualifying time. Will be awarded Provincial Half Colours.")
elif completion_time <= 110:        # 'less than or equal to'
       print("You are within the 10 minutes of the qualifying time. Will be awarded Provincial Scroll.")
elif completion_time >= 111:        # 'more than or equal to'
       print("You are not within qualifying time. Thanks for partecipating.")

print(f"Completion:{completion_time} minutes")


