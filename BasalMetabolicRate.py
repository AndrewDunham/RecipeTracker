

user_gender = input("What biological gender are you?(male or female)")
weight = int(input("What is your weight in kg?"))
height = int(input("What is your height in cm?"))
age = int(input("What is your age in years?"))

if user_gender == "male":
  BMR = 88.362 + (13.397 * weight) + (4.799 * height) – (5.677 * age)

else:
  BMR = 447.593 + (9.247 * weight) + (3.098 * height) – (4.330 * age)
    
print("You burn " + BMR + " calories a day")
