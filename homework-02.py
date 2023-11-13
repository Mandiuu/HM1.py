# Carla Mandiola 
# November 6
# "Homework 2"


# 1. How old the user is: 

year_of_birth = input("What year were you born?: ")
year_of_birth = int(year_of_birth)
age = int(2023 - year_of_birth)
print (f"I bet you didn't know you're {age} years old.")

# 2. In that time, how many times the user's heart has beaten.

# I found here the answer about the heartbeat of a human https://to.pbs.org/49kzeKG
# It's about 35 million times in a year <3

heart = age * 35000000
print("Since you were born, your heart has beaten about", heart, "times. Can you believe it?")

# 3. In that time, how many times a blue whale's heart has beaten.

# I got the information about the Blue Whale heartbeat here  https://bit.ly/3FNkmae
# The heartbeat of a whale is 33 per minute. I calculated how many minutes a year has, and it's 525600

whale = age * (33*525600)
print ("In that time, a blue whale's heart has beaten", whale, "times.")

# 4.  In that time, how many times a rabbit's heart has beaten. If the answer to rabbit heartbeats is more than a billion, say "XXX billion" instead of the very long raw number

# The heartbeat of a rabbit goes from 140 to 180 per minute, so I calculated it as 160. I converted the result into billions and then round it.

rabbit = age * round(160*525600/1000000000,2)
print ("Since you are alive, the heartbeat of a random rabbit has been about", rabbit, "billion times. ")


# 5. There are several ways to calculate and format/display numbers in Python – string addition, f-strings, commas, etc etc etc. Redo one of the above questions above with another technique and briefly explain the pros and cons of each approach.

# For the first question, I did it using the library datetime and it worked, but it was complicated, and also, the result wasn't an int.
# The good part of using datetime is that it can be more precise if, for example, I need to compare it with the day, month, and year of a person. 

#from datetime import datetime
#year_of_birth = input("What year were you born? (YYYY): ")
#year_of_birth = datetime.datetime.strptime(year_of_birth, '%Y')
#age = datetime.datetime.now().year - year_of_birth.year
#print ("Hello! You're %(age)s years old." % {"age": age})


#6. Whether they are the same age as you, older or younger
# If older or younger, how many years difference

if age == 34:
    print("Yey! We are the same age.")

if age > 34:
   print("Ok, boomer. You are", abs(age-34), "years older than me.")

elif age < int(34):
   print("You are", abs(age-34) , "years younger than me. Wow")

# If they were born in an even or odd year

if (year_of_birth % 2) == 0:
  print ("You were born in an even year")

else:
   print ("Oddly, your year of birth is odd")


# 7. How many times there has been a president from the Democratic Party in office since they were born (1980 onward, and each president only counts once)

#1980-1981	Jimmy Carter	
#1993-2000	Bill Clinton	
#2009-2017	Barack Obama	
#2021-2023  Joe Biden

n = year_of_birth

if n in range(1980, 1981): 
    print("You have seen 4 Democrat Presidents")

if n in range(1982, 2008):
     print("You have seen 3 Democrat Presidents")

if n in range(2009, 2020):
     print("You have seen 2 Democrat Presidents")

elif n in range(2021, 2023):
    print("You have seen only 1 Democrat President")


#8. Which US President was in office when they were born (1980 onward)
#1980-1981	Jimmy Carter	
#1981-1989	Ronald Reagan	
#1989-1993	George Bush	
#1993-2001	Bill Clinton	
#2001-2009	George W. Bush	
#2009-2017	Barack Obama	
#2017-2021	Donald J. Trump	
#2021-	Joseph R. Biden

if n in range(1980, 1981): 
    print(f"Did you know that Jimmy Carter was the US President when you were born?!")

if n in range(1981, 1989): 
    print(f"Did you know that Ronald Reagan was the US President when you were born?!")

if n in range(1990, 1993): 
    print(f"Did you know that George Bush was the US President when you were born?!")

if n in range(1994, 2001): 
    print(f"Did you know that Bill Clinton was the US President when you were born?!")

if n in range(2002, 2009): 
    print(f"Did you know that George W. Bush was the US President when you were born?!")

if n in range(2010, 2017): 
    print(f"Did you know that Barack Obama was the US President when you were born?!")

if n in range(2018, 2021): 
    print(f"Did you know that Donald J. Trump was the US President when you were born?!")

elif n in range(2021, 2023): 
    print(f"Did you know that Joseph R. Biden was the US President when you were born?! Wait, you shouldn't even been here, you are TOO young.")



#9 #Can you think of another approach to #7 and/or #8 that you could have tried? Why is yours better?
# I honestly can't think of a better way to do it besides a range of numbers because I want to believe it's shorter 

#10 If someone says they were born in the future, ask them for their year of birth again. Assume they'll do it right the second time.

future = input("So, you say you come from the future. What year were you born?: ")
future = int(future)

if future < 2023:
   print("Hey, that's not the future! Try it again")

future2 = input("One more time, what year were you born?: ")
future2 = int(future2)

if future2 > 2023:
    print("Wow that's scary, you really come from the future. Am I ever going to be rich?")
