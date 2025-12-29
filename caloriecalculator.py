def calculategoal():
     print("\nWelcome to the Calorie Goal Calculator!\n")
     print("I will give you some prompts to fill in and you will\nbe given the essential information for your fitness journey!\n")

     # Code allows user to specify gender, an error pops up if neither 'Male' or 'Female'.
     while True:
          try:
               gender = input("Enter your gender: ")
               if gender.lower() != "male" and gender.lower() != "female":
                    print("Gender must be male or female.\n")
                    continue
               break
          except ValueError:
               print("Try again.")
          break
     # Code allows user to specify age, and check if the age is valid and above 0.
     while True:
          try:
               age = int(input("Enter your age: "))
               if age < 8:
                    print("Age must be greater than 8.\n")
                    continue
               break
          except ValueError:
               print("Try again.")
          break
     
     # Code checks if the user prefers the 'imperial' or 'metric' system for measurement.
     while True:
          try:
               system = input("Imperial or Metric system: ").lower()
               if system not in ["imperial", "metric"]:
                    print("Please enter imperial or metric.\n")
                    continue
               break
          except ValueError:
               print("Try again.")
          break     
          
     # Displays either 'Imperial' or 'Metric' based measurements based on what the user selected.
     while True:
          if system == 'imperial':
               print("\nPlease enter feet, inches, and weight separately.\n")
               try:
                    feet = int(input("Feet: "))
                    inches = int(input("Inches: "))
                    lbs = float(input("Weight (ex: 160.2): "))
                    if feet < 3 and feet > 8:
                         print("Feet must fall within 3 and 8.")
                         continue
                    elif inches < 0 and inches > 11:
                         print("Inches must be between 0 and 11.")
                         continue
                    elif lbs <= 0:
                         print("Weight must be greater than 0.")
                         continue
                    break
               except ValueError:
                    print("Value must be a whole number.")
          elif system == 'metric':
               print("\nPlease enter centimeters (height) and kilograms (weight) separately.\n")
               try:
                    centimeters = float(int("Centimeters (ex: 184.2): "))
                    kilograms = float(input("Kilograms (ex: 76.7): "))
                    if centimeters < 90:
                         print("Centimeters must be greater than 90.")
                         continue
                    elif kilograms < 0:
                         print("Kilograms must be greater than 0.")
                         continue
                    break
               except ValueError:
                    print("Value must be a decimal.")
               break
          else:
               print("Imperial or Metric is not defined.")
          break

     # Code allows the user to select a plan, and define a calorie surplus/deficit number.
     while True:
          print("""
                
     PLAN           |            DESCRIPTION
     -----------------------------------------------------------
     Intense Cut    |       Risk muscle loss, extreme fat loss.
     Slow Cut       |       Preserve muscle, while losing fat.
     Recomp         |       Build muscle, while losing fat.
     Lean Bulk      |       Slow muscle gain, limited fat gain.
     Dirty Bulk     |       Quick muscle and fat gain.\n
     
          """)
          plan = input("Look at the table above and enter your goal here: ").lower()

          if plan not in ["intense cut", "slow cut", "recomp", "lean bulk", "dirty bulk"]:
               print("Please provide a plan from the list.\n")

          if plan == "intense cut":
               try:
                    print("\nProvide a calorie deficit for your Intense Cut.")
                    intakenum = int(input("Enter a number between -700 and -1000: "))
                    if intakenum < -1000:
                         print("Number must be greater than -1000.")
                         continue
                    elif intakenum > -700:
                         print("Number must be less than -700.")
                         continue
                    break
               except:
                    print("Enter a valid number.")
               break
          elif plan == "slow cut":
               try:
                    print("\nProvide a calorie deficit for your Slow Cut.")
                    intakenum = int(input("Enter a number between -600 and -300: "))
                    if intakenum < -1000:
                         print("Number must be greater than -600.")
                         continue
                    elif intakenum > -700:
                         print("Number must be less than -300.")
                         continue
                    break
               except:
                    print("Enter a valid number.")
               break
          elif plan == "recomp":
               try:
                    print("\nProvide a calorie deficit for your Recomp.")
                    intakenum = int(input("Enter a number between -200 and 0: "))
                    if intakenum < -200:
                         print("Number must be greater than -200.")
                         continue
                    elif intakenum > 0:
                         print("Number must be less than 0.")
                         continue
               except:
                    print("Enter a valid number.")
               break
          elif plan == "lean bulk":
               try:
                    print("\nProvide a calorie surplus for your Lean Bulk.")
                    intakenum = int(input("Enter a number between 200 and 450: "))
                    if intakenum < 200:
                         print("Number must be greater than 200.")
                         continue
                    elif intakenum > 450:
                         print("Number must be less than 450.")
                         continue
               except:
                    print("Enter a valid number.")
               break
          elif plan == "dirty bulk":
               try:
                    print("\nProvide a calorie surplus for your Dirty Bulk.")
                    intakenum = int(input("Enter a number between 500 and 750: "))
                    if intakenum < 500:
                         print("Number must be greater than 500.")
                         continue
                    elif intakenum > 750:
                         print("Number must be less than 750.")
                         continue
               except:
                    print("Enter a valid number.")
               break
          else:
               print("One of the plans are not available.")
          break

     while True:
          # Code calculates weight and height based on if the user selected 'imperial' or 'metric' system earlier.
          if system == "imperial":
               weight_kg = (lbs/2.20462)
               height_cm = (feet*30.48) + (inches*2.54)
          elif system == "metric":
               weight_kg = weight_kg
               height_cm = height_cm
          else:
               raise ValueError("System must be 'Imperial' or 'Metric'.")
          break

     # Code calcualtes Basic Metabolism Rate based on the gender the user selected.
     while True:
          if gender == "male":
               bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) + 5
          elif gender == "female":
               bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) - 161
          else:
               raise ValueError("Gender must be 'Male' or 'Female'.")
          break

     # This code finishes the calculation of calories needed based on activity level.
     # Displays a table of activity level options and allows the user to select an option.
     while True:
          print("""
                
     ACTIVITY LEVEL   |       DESCRIPTION
     -----------------------------------------------------------
     Sedentary        |       No lifting
     Light            |       Exercise 1-3x per week.
     Moderate         |       Exercise 3-5x per week.
     High             |       Exercise 6-7x per week.
     Intense          |       Extreme exercise 7x per week.
     
          """)
          activity = input("Enter your activity level: ").lower()

          # Code checks users input and if not one of the options, gives a error.  
          if activity not in ["sedentary", "light", "moderate", "high", "intense"]:
               print("Please provide one of the options in the 'ACTIVITY LEVEL' column.\n")
          
          # Code defines multipliers for the activity levels.
          activity_factors = {
               "sedentary": 1.15,
               "light": 1.36,
               "moderate": 1.52,
               "high": 1.71,
               "intense": 1.87
               }
          
          # Code checks if activity level is in the activity_factors list, gives error if not.
          if activity not in activity_factors:
               raise ValueError("Invalid activity level")
          
          # Calculates the Total Daily Expenditure for user.
          tdee = bmr * activity_factors[activity]
          # Calculates the total calories a user needs for their fitness goal.
          calories = tdee + intakenum
          # Code prints a list showing all the requirements for their fitness goal.
          print(f"\n\nDAILY REQUIREMENTS:\nCalories: {calories:,.0f} kcal")
          break

# Runs the calcualtion program and ends with prompt allowing user to continue or not.   
calculategoal()
calculateagain = input("\nWould you like to calculate again? (y/n): ")
if calculateagain != "y":
     print("Good luck on your fitness journey!\n")
