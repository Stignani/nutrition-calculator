# Nutrition Calculator

#variables
sex = input("Enter your sex (male/female): ").lower()
age = int(input("Enter your age: "))

weight = float(input("Enter your weight(lbs): "))
weight_kg = weight * 0.453592  # Convert weight to kilograms

height = float(input("Enter your height(in): "))
height_cm = height * 2.54  # Convert height to centimeters

#assigning multpliers based on activity level
activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ").lower()
if activity_level == "sedentary":
    activity_multiplier = 1.2
elif activity_level == "lightly active":
    activity_multiplier = 1.375
elif activity_level == "moderately active":
    activity_multiplier = 1.55
elif activity_level == "very active":
    activity_multiplier = 1.725
elif activity_level == "extra active":
    activity_multiplier = 1.9
else:
    print("Invalid activity level input. Please enter one of the specified options.")
    exit() 

#Determining Goal for Calorie Adjustment and Mcros
goal = input("Enter your goal (lose, maintain, gain): ").lower() 
if goal == "lose":
    calorie_adjustment = -500
elif goal == "maintain":
    calorie_adjustment = 0
elif goal == "gain":    calorie_adjustment = 300
else:
    print("Invalid goal input. Please enter 'lose', 'maintain', or 'gain'.")
    exit()


#Calculating BMR
if sex == "male":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
elif sex == "female":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161  
else:
    print("Invalid sex input. Please enter 'male' or 'female'.")
    exit()


#Calculating Daily Calories
calories = bmr * activity_multiplier +calorie_adjustment
print(f"To achieve your goal, you should consume approximately {calories:,.0f} calories per day.")

#Calculating Macros
if goal == "lose":
    protein = weight 
    fat = calories * 0.25/9
    carbs = (calories - (protein * 4 + fat * 9)) / 4 
elif goal == "maintain":
    protein = weight * 0.8
    fat = calories * 0.25/9
    carbs = (calories - (protein * 4 + fat * 9)) / 4
elif goal == "gain":
    protein = weight * 1.2
    fat = calories * 0.25/9
    carbs = (calories - (protein * 4 + fat * 9)) / 4

print(f"Your daily macronutrient intake should be approximately:\nProtein: {protein:.2f} grams\nFat: {fat:.2f} grams\nCarbohydrates: {carbs:.2f} grams")