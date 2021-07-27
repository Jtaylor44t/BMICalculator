def bmicalc():
    print()
    name = input("What is your name?: ").lower()
    age = input(f"{name.title()}, how old are you?: ")
    weight = int(input(f"{name.title()}, how much do you weigh?: "))
    height = int(input(f"{name.title()}, how tall are you in inches? (If you don't know, figure it out...): "))
    print()
    print(f"{name.title()}, you are {age} years old.")
    print(f"{name.title()}, you weigh {weight} pounds.")
    print(f"{name.title()}, you are {height} inches tall.")
    print()
    bmi = round((weight /(height*height)) * int(703.069579642))
    if bmi <= 18.5:
        print("Your BMI is below 18.5. Which means you are Underweight. Eat more steak.")
    elif 18.5 <= bmi <= 24.9:
        print("Your BMI is between 18.5 and 24.9. Which means you have a Normal BMI. Good for you.")
    elif 25.0 <= bmi <= 29.9:
        print("Your BMI is between 25.0 and 29.9. Which means you are Overweight. Watch them calories.")
    elif 30 <= bmi <= 39.99:
        print("Your BMI is between 30.0 and 39.99 or above. Which means you are Obese.")
    elif bmi >= 40:
        print("Your BMI is 40.0 or above. Which means you are morbidly obese.")
    print()
bmicalc()





 #Formula: Weight (lb) / [height (in)]2 x 703. Calculate BMI by dividing weight in pounds (lbs) by height in inches (in) 
 #squared and multiplying by a conversion factor of 703.
 #calculate BMI and then tell you your rating based off age, weight, and height. use if conditionals (obese, overweight,
 # underweight, etc.) 