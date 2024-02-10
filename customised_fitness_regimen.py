"""
Author: Christy Lee
LinkedIn: https://www.linkedin.com/in/christy-lee-798b53276/
GitHub Repository: https://github.com/christy511/Customised-Fitness-Regimen.git
"""

import math

def fat_loss():
   print("Plate thrusters (15 reps x 3 sets)")
   print("Mountain climbers (20 reps x 3 sets)")
   print("Box jumps (10 reps x 3 sets)")
   print("Lunges (10 reps x 3 sets)")
   print("Renegade rows (10 reps x 3 sets)")
   print("Press ups (15 reps x 3 sets)")
   print("Treadmill (10 mins x 3 sets)")
   print("Supermans (10 reps x 3 sets)")
   print("Crunches (10 reps x 3 sets)")

def stretch_and_relax():
   print("Quad stretchs (2 mins x 3 sets)")
   print("Hamstring stretchs (2 mins x 3 sets)")
   print("Chest and shoulder stretchs (2 mins x 2 sets)")
   print("Upper back stretchs (3 mins x 2 sets)")
   print("Biceps stretchs (2 mins x 2 sets)")
   print("Triceps stretchs (2 mins x 3 sets)")
   print("Hip flexors (2 mins x 3 sets)")
   print("Calf stretchs (2 mins x 3 sets)")
   print("Lower back stretchs (2 mins x 3 sets)")

def high_intensity_exercises():
   print("Jumping jacks (20 reps x 4 sets)")
   print("Sprints (20 reps x 3 sets)")
   print("Mountain climbers (20 reps x 4 sets)")
   print("Squat jumps (20 reps x 4 sets)")
   print("Lunges (20 reps x 3 sets)")
   print("Crunches (20 reps x 3 sets)")
   print("Treadmill (15 mins x 2 sets)")
   print("Side planks (15 reps x 3 sets)")
   print("Burpees (15 reps x 3 sets)")

def strong_legs():
   print("Back squats (10 reps x 5 sets)")
   print("Hip thrusts (12 reps x 3 sets)")
   print("Overhead presses (10 reps x 5 sets)")
   print("Rack pulls (10 reps x 5 sets)")
   print("Squats (10 reps x 4 sets)")
   print("Dumbbell lunges (10 reps x 3 sets)")
   print("Leg curls (15 reps x 3 sets)")
   print("Standing calf raises (20 reps x 2 sets)")
   
def strong_abs():
   print("Cross crunchs (12 reps x 3 sets)")
   print("Knee ups (15 reps x 5 sets)")
   print("Hip thrusts (15 reps x 3 sets)")
   print("Mountain climbers (15 reps x 3 sets)")
   print("Vertical hip thrusts (12 reps x 3 sets)")
   print("Bicycles (15 mins x 2 sets)")
   print("Front planks (15 mins x 3 sets)")
   print("Dragon flags (12 reps x 4 sets)")
   print("Reverse crunches (10 reps x 3 sets)")

def strong_shoulders_arms():
   print("Bench presses (10 reps x 5 sets)")
   print("Triceps dips (10 reps x 5 sets)")
   print("Incline dumbbell presses (12 reps x 3 sets)")
   print("dumbbell flyes (15 reps x 3 sets)")
   print("Triceps extensions (15 reps x 3 sets)")
   print("Pull ups (10 reps x 5 sets)")
   print("Treadmill (15 mins x 2 sets)")
   print("Bent over rows (10 reps x 5 sets)")
   print("Chin ups (10 reps x 3 sets)")

def male_less_18():
   print("High knees (20 reps x 3 sets)")
   print("Squats (10 reps x 3 sets)")
   print("Calf raises (10 reps x 3 sets)")
   print("Scissor jumps (12 reps x 3 sets)")
   print("Burpees (10 reps x 3 sets)")
   print("Treadmill (10 mins x 2 sets)")

def female_less_18():
   print("Squats (10 reps x 3 sets)")
   print("Crunches (10 reps x 2 sets)")
   print("Jumping jacks (10 reps x 3 sets)")
   print("Push ups (10 reps x 2 sets)")
   print("Burpees (10 reps x 3 sets)")
   print("Treadmill (10 mins x 2 sets)")

def male_above_18():
   print("Standing biceps curls (20 reps x 3 sets)")
   print("Seated incline curls (18 reps x 3 sets)")
   print("Seated dumbbell presses (12 reps x 3 sets)")
   print("Leg presses (15 reps x 3 sets)")
   print("Bench presses (10 reps x 4 sets)")
   print("Tricep kickbacks (15 reps x 3 sets)")
   print("Hip thrusts (12 reps x 3 sets)")
   print("Seated rows (10 reps x 4 sets)")

def female_above_18():
   print("Lateral raises (15 reps x 3 sets)")
   print("Reverse flyes (12 reps x 3 sets)")
   print("Hip thrusts (12 reps x 3 sets)")
   print("Incline dumbbell presses (15 reps x 3 sets)")
   print("Squats (10 reps x 4 sets)")
   print("Dumbbell lunges (10 reps x 3 sets)")
   print("Leg presses (12 reps x 3 sets)")
   print("Dumbbell presses (10 reps x 4 sets)")

def training():
   print("What do you want to get out of your training? ")
   print("    1. Your goal is losing weight")
   print("    2. Your goal is to staying calm and relax")
   print("    3. Your goal is increasing your heart rate")
   print("    4. Your goal is having stronger legs")
   print("    5. Your goal is having stronger ABS")
   print("    6. Your goal is having stronger shoulders and arms")

name = input("Please enter your name: ")
while not name.isalpha():
    print("Error: Only accept alphabetical characters and spaces for name")
    print()
    name = input("Please enter your name: ")

print()

age = int(input("Please enter your age: "))
while age < 1 or age > 110:
   print("Error: The age is a number between 0 to 110")
   print()
   age = int(input("Please enter your age: "))

print()
x = 100
if age <= 60:
    x = 100/100
if 60 < age <= 65:
    x = ((x - (0 + ((age - 60)*1)))/100)
if 65 < age <= 75:
    x = ((x - (5 + ((age - 65)*2)))/100)
if 75 < age <= 80:
    x = ((x - (25 + ((age - 75)*3)))/100)
if 80 < age <= 90:
    x = ((x - (40 + ((age - 80)*4)))/100)
if age > 90:
    x = ((x - 80)/100) 
sex = input("Please enter your biological sex (female/male): ")

while sex != "male" and sex != "female":
   print("Error: Please enter valid input")
   print()
   sex = input("Please enter your biological sex (female/male): ")
print()
training()
num = int(input("Choose a number between 1 to 6: "))

while num < 1 or num > 6:
   print("Error - It can only be a number between 1 to 6")
   print()
   training()
   num = int(input("Choose a number between 1 to 6: "))
print()
days = int(input("How many days per week you can train: "))

while days < 1 or days > 7:
   print("Error: It can only be a number between 1 to 7")
   print()
   days = int(input("How many days per week you can train: "))

print()
def greeting(name: str)-> str:
    return f'Hello {name}! Here is your training:'

print(greeting(name))
i = 1
if (num == 1):
    while 0 < days <= 7:
        print('-------------------------------------------------------------------------------------')
        print("Day",i)
        if ((i+1) % 2) == 0:
            print("Gym workout for fat loss")
            print()
            print(f"Plate thrusters ({math.ceil(15*x)} reps x 3 sets)")
            print(f"Mountain climbers ({math.ceil(20*x)} reps x 3 sets)")
            print(f"Box jumps ({math.ceil(10*x)} reps x 3 sets)")
            print(f"Lunges ({math.ceil(10*x)} reps x 3 sets)")
            print(f"Renegade rows ({math.ceil(10*x)} reps x 3 sets)")
            print(f"Press ups ({math.ceil(15*x)} reps x 3 sets)")
            print(f"Treadmill ({math.ceil(10*x)} mins x 3 sets)")
            print(f"Supermans ({math.ceil(10*x)} reps x 3 sets)")
            print(f"Crunches ({math.ceil(10*x)} reps x 3 sets)")
        i = i+1
        days = days -1

        if ((i+1) % 2) == 0:
            if (sex == "male"):
                if (age>=18):
                    print("Gym workout for a male at least 18 years old")
                    print()
                    print(f"Standing biceps curls ({math.ceil(20*x)} reps x 3 sets)")
                    print(f"Seated incline curls ({math.ceil(18*x)} reps x 3 sets)")
                    print(f"Seated dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                    print(f"Leg presses ({math.ceil(15*x)} reps x 3 sets)")
                    print(f"Bench presses ({math.ceil(10*x)} reps x 4 sets)")
                    print(f"Tricep kickbacks ({math.ceil(15*x)} reps x 3 sets)")
                    print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                    print(f"Seated rows ({math.ceil(10*x)} reps x 4 sets)")

                else:
                    print("Gym workout for a male younger than 18 years old")
                    print()
                    print(f"High knees ({math.ceil(20*x)} reps x 3 sets)")
                    print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Calf raises ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Scissor jumps ({math.ceil(12*x)} reps x 3 sets)")
                    print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")
            else:
                if (age >= 18):
                    print("Gym workout for a female at least 18 years old")
                    print()
                    print(f"Lateral raises ({math.ceil(15*x)} reps x 3 sets)")
                    print(f"Reverse flyes ({math.ceil(12*x)} reps x 3 sets)")
                    print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                    print(f"Incline dumbbell presses ({math.ceil(15*x)} reps x 3 sets)")
                    print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                    print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Leg presses ({math.ceil(12*x)} reps x 3 sets)")
                    print(f"Dumbbell presses ({math.ceil(10*x)} reps x 4 sets)")

                else:
                    print("Gym workout for a female younger than 18 years old")
                    print()
                    print("Squats ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Crunches ({math.ceil(10*x)} reps x 2 sets)")
                    print(f"Jumping jacks ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Push ups ({math.ceil(10*x)} reps x 2 sets)")
                    print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                    print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")

else:
    if (num == 2):
        while 0 < days <= 7:
            print('-------------------------------------------------------------------------------------')
            print("Day",i)
            if ((i+1) % 2 == 0):
                print("Gym workout for stretch and relax")
                print()
                print(f"Quad stretchs ({math.ceil(2*x)} mins x 3 sets)")
                print(f"Hamstring stretchs ({math.ceil(2*x)} mins x 3 sets)")
                print(f"Chest and shoulder stretchs ({math.ceil(2*x)} mins x 2 sets)")
                print(f"Upper back stretchs ({math.ceil(3*x)} mins x 2 sets)")
                print(f"Biceps stretchs ({math.ceil(2*x)} mins x 2 sets)")
                print(f"Triceps stretchs ({math.ceil(2*x)} mins x 3 sets)")
                print(f"Hip flexors ({math.ceil(2*x)} mins x 3 sets)")
                print(f"Calf stretchs ({math.ceil(2*x)} mins x 3 sets)")
                print(f"Lower back stretchs ({math.ceil(2*x)} mins x 3 sets)")
            i = i + 1 
            days = days - 1

            if ((i+1) % 2) == 0:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        print()
                        print(f"Standing biceps curls ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Seated incline curls ({math.ceil(18*x)} reps x 3 sets)")
                        print(f"Seated dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Bench presses ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Tricep kickbacks ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Seated rows ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        print()
                        print(f"High knees ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Calf raises ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Scissor jumps ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")
                else:
                    if (age >= 18):
                        print("Gym workout for a female at least 18 years old")
                        print()
                        print(f"Lateral raises ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Reverse flyes ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Incline dummbell presses ({math.ceil(50*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Dumbbell presses ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a female younger than 18 years old")
                        print()
                        print("Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Crunches ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Jumping jacks ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Push ups ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")

    if (num == 3):
        while 0 < days <= 7:
            print('-------------------------------------------------------------------------------------')
            print("Day",i)
            if ((i+1) % 2 == 0):
                print("Gym workout for high-intensity exercises")
                print()
                print("Jumping jacks ({math.ceil(20*x)} reps x 4 sets)")
                print("Sprints ({math.ceil(20*x)} reps x 3 sets)")
                print("Mountain climbers ({math.ceil(20*x)} reps x 4 sets)")
                print("Squat jumps ({math.ceil(20*x)} reps x 4 sets)")
                print("Lunges ({math.ceil(20*x)} reps x 3 sets)")
                print("Crunches ({math.ceil(20*x)} reps x 3 sets)")
                print("Treadmill ({math.ceil(15*x)} mins x 2 sets)")
                print("Side planks ({math.ceil(15*x)} reps x 3 sets)")
                print("Burpees (math.ceil(15*x)} reps x 3 sets)")
            i = i + 1
            days = days - 1

            if ((i+1) % 2) == 0:
                if(sex == "male"):
                    if (age >= 18):
                        print("Gym workout for a male at least 18 years old")
                        print()
                        print(f"Standing biceps curls ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Seated incline curls ({math.ceil(18*x)} reps x 3 sets)")
                        print(f"Seated dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Bench presses ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Tricep kickbacks ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Seated rows ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        print()
                        print(f"High knees ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Calf raises ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Scissor jumps ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")
                else:
                    if (age >= 18):
                        print("Gym workout for a female at least 18 years old")
                        print()
                        print(f"Lateral raises ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Reverse flyes ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Incline dummbell presses ({math.ceil(50*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Dumbbell presses ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a female younger than 18 years old")
                        print()
                        print("Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Crunches ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Jumping jacks ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Push ups ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")

    if(num == 4):
        while 0 < days <= 7:
            print('-------------------------------------------------------------------------------------')
            print("Day",i)
            if ((i+1) % 2 == 0):
                print("Gym workout for strong legs")
                print(f"Back squats ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                print(f"Overhead presses ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Rack pulls ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                print(f"Leg curls ({math.ceil(15*x)} reps x 3 sets)")
                print(f"Standing calf raises ({math.ceil(20*x)} reps x 2 sets)")
            i = i + 1
            days = days - 1
            
            if ((i+1) % 2) == 0:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        print()
                        print(f"Standing biceps curls ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Seated incline curls ({math.ceil(18*x)} reps x 3 sets)")
                        print(f"Seated dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Bench presses ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Tricep kickbacks ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Seated rows ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        print()
                        print(f"High knees ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Calf raises ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Scissor jumps ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")
                else:
                    if (age >= 18):
                        print("Gym workout for a female at least 18 years old")
                        print()
                        print(f"Lateral raises ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Reverse flyes ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Incline dummbell presses ({math.ceil(50*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Dumbbell presses ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a female younger than 18 years old")
                        print()
                        print("Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Crunches ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Jumping jacks ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Push ups ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")

    if(num == 5):
        while 0 < days <= 7:
            print('-------------------------------------------------------------------------------------')
            print("Day",i)
            if ((i+1) % 2 == 0):
                print("Gym workout for strong ABS")
                strong_abs()
                print(f"Cross crunchs ({math.ceil(12*x)} reps x 3 sets)")
                print(f"Knee ups ({math.ceil(15*x)} reps x 3 sets)")
                print(f"Hip thrusts ({math.ceil(15*x)} reps x 3 sets)")
                print(f"Mountain climbers ({math.ceil(15*x)} reps x 3 sets)")
                print(f"Vertical hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                print(f"Bicycles ({math.ceil(15*x)} mins x 2 sets)")
                print(f"Front planks ({math.ceil(15*x)} mins x 3 sets)")
                print(f"Dragon flags ({math.ceil(12*x)} reps x 4 sets)")
                print(f"Reverse crunches ({math.ceil(10*x)} reps x 3 sets)")
            i = i + 1
            days = days - 1
 
            if ((i+1) % 2) == 0:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        print()
                        print(f"Standing biceps curls ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Seated incline curls ({math.ceil(18*x)} reps x 3 sets)")
                        print(f"Seated dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Bench presses ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Tricep kickbacks ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Seated rows ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        print()
                        print(f"High knees ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Calf raises ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Scissor jumps ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")
                else:
                    if (age >= 18):
                        print("Gym workout for a female at least 18 years old")
                        print()
                        print(f"Lateral raises ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Reverse flyes ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Incline dummbell presses ({math.ceil(50*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Dumbbell presses ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a female younger than 18 years old")
                        print()
                        print("Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Crunches ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Jumping jacks ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Push ups ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")

    if(num == 6):
        while 0 < days <= 7:
            print('-------------------------------------------------------------------------------------')
            print("Day",i)
            if ((i+1) % 2 == 0):
                print("Gym workout for strong shoulders and arms")
                print(f"Bench presses ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Triceps dips ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Incline dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                print(f"dumbbell flyes ({math.ceil(15*x)} reps x 3 sets)")
                print(f"Triceps extensions ({math.ceil(15*x)} reps x 3 sets)")
                print(f"Pull ups ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Bent over rows ({math.ceil(10*x)} reps x 5 sets)")
                print(f"Chin ups ({math.ceil(10*x)} reps x 3 sets)")
            i = i + 1
            days = days - 1
 
            if ((i+1) % 2) == 0:
                if(sex == "male"):
                    if(age>=18):
                        print("Gym workout for a male at least 18 years old")
                        print()
                        print(f"Standing biceps curls ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Seated incline curls ({math.ceil(18*x)} reps x 3 sets)")
                        print(f"Seated dumbbell presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Bench presses ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Tricep kickbacks ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Seated rows ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a male younger than 18 years old")
                        print()
                        print(f"High knees ({math.ceil(20*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Calf raises ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Scissor jumps ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")
                else:
                    if (age >= 18):
                        print("Gym workout for a female at least 18 years old")
                        print()
                        print(f"Lateral raises ({math.ceil(15*x)} reps x 3 sets)")
                        print(f"Reverse flyes ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Hip thrusts ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Incline dummbell presses ({math.ceil(50*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 4 sets)")
                        print(f"Dumbbell lunges ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Leg presses ({math.ceil(12*x)} reps x 3 sets)")
                        print(f"Dumbbell presses ({math.ceil(10*x)} reps x 4 sets)")
                    else:
                        print("Gym workout for a female younger than 18 years old")
                        print()
                        print("Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Squats ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Crunches ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Jumping jacks ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Push ups ({math.ceil(10*x)} reps x 2 sets)")
                        print(f"Burpees ({math.ceil(10*x)} reps x 3 sets)")
                        print(f"Treadmill ({math.ceil(10*x)} reps x 2 sets)")

def bye(name: str)-> str:
    return f'-------------------------------------------------------------------------------------\n\nBye {name}.'

print(bye(name))