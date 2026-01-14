# Main Calorie Calcualtion function.
def calculate_calories():
     print("\nWelcome to the Calorie Goal Calculator!\n")
     print("I will give you some prompts to fill in and you will\nbe given the essential information for your fitness journey!\n")

     # User enters Gender, Age, and Measurement System
     while True:
          try:
               gender = input("Enter your gender (m/f): ").lower()
               age = int(input("Enter your age: "))
               system = input("Imperial or Metric system (i/m): ").lower()
               # Checks if gender is male or female:
               if gender not in ["male","m"] and gender not in ["female","f"]:
                    print("Gender must be Male or Female.\n")
                    continue
               # Checks if age is 8 or older:
               if age <= 8:
                    print("Age must be 8 or older.\n")
                    continue
               # Checks if measurement is imperial or metric:
               if system not in ["imperial","i","metric","m"]:
                    print("Please enter imperial or metric.\n")
                    continue
               break
          # Give an error if there is an incorrect value:
          except ValueError:
               print("Try again.\n")
          break
          
     # Enter height and weight that is aligned with selected measurement system.
     while True:
          # If the imperial system was selected, enter feet, inches, and lbs:
          if system in ["imperial","i"]:
               print("\nPlease enter feet, inches, and weight separately.\n")
               try:
                    feet = int(input("Feet: "))
                    inches = int(input("Inches: "))
                    lbs = float(input("Weight in lbs (ex: 160.2): "))
                    # Checks if feet is between 3 and 8:
                    if feet < 3 and feet > 8:
                         print("Feet must fall within 3 and 8.\n")
                         continue
                    # Checks if inches are between 0 and 11:
                    elif inches < 0 and inches > 11:
                         print("Inches must be between 0 and 11.\n")
                         continue
                    # Checks if weight is greater than 0:
                    elif lbs <= 0:
                         print("Weight must be greater than 0.\n")
                         continue
                    break
               # Give an error if there is an incorrect value:
               except ValueError:
                    print("Value must be a whole number.\n")
          # If the metric system was selected, enter centimeters and kilograms:
          elif system in ["metric","m"]:
               print("\nPlease enter centimeters (height) and kilograms (weight) separately.\n")
               try:
                    centimeters = float(int("Centimeters (ex: 184.2): "))
                    kilograms = float(input("Kilograms (ex: 76.7): "))
                    # Checks if centimeters are greater than 90:
                    if centimeters < 90:
                         print("Centimeters must be greater than 90.\n")
                         continue
                    # Checks if kilograms are greater than 0:
                    elif kilograms < 0:
                         print("Kilograms must be greater than 0.\n")
                         continue
                    break
               # Give an error if there is an incorrect value:
               except ValueError:
                    print("Value must be a decimal.\n")
               break
          break

     # Displays workout goal table and allows user to specify workout goal:
     while True:
          print("""
     GOAL           |            DESCRIPTION
     -----------------------------------------------------------
     Intense Cut    |       Risk muscle loss, extreme fat loss.
     Slow Cut       |       Preserve muscle, while losing fat.
     Recomp         |       Build muscle, while losing fat.
     Lean Bulk      |       Slow muscle gain, limited fat gain.
     Dirty Bulk     |       Quick muslce and fat gain.\n
          """)
          goal = input("Enter your goal here (ic/sc/r/lb/db): ").lower()
          # If one of the goals are not selected:
          if goal not in ["intense cut","ic", "slow cut","sc", "recomp","r", "lean bulk","lb", "dirty bulk","db"]:
               print("Please provide a plan from the list.\n")
          # If goal is intense cut:
          if goal in ["intense cut", "ic"]:
               try:
                    print("\nProvide a calorie deficit for your Intense Cut.")
                    # User provides calorie deficit between -700 and -1000:
                    intakenum = int(input("Enter a number between -700 and -1000: "))
                    # Display error when the number is less than -1000:
                    if intakenum < -1000:
                         print("Number must be greater than -1000.\n")
                         continue
                    # Display error when the number is greater than -700:
                    elif intakenum > -700:
                         print("Number must be less than -700.\n")
                         continue
                    break
               # If number is not an integer:
               except ValueError:
                    print("Enter a valid number.\n")
               break
          # If goal is slow cut:
          elif goal in ["slow cut", "sc"]:
               try:
                    print("\nProvide a calorie deficit for your Slow Cut.")
                    # User enters calorie deficit between -600 and -300:
                    intakenum = int(input("Enter a number between -600 and -300: "))
                    # Display error when the number is less than -600:
                    if intakenum < -1000:
                         print("Number must be greater than -600.\n")
                         continue
                    # Display error when the number is greater than -300:
                    elif intakenum > -700:
                         print("Number must be less than -300.\n")
                         continue
                    break
               # If number is not an integer:
               except ValueError:
                    print("Enter a valid number.\n")
               break
          # If goal is recomp:
          elif goal in ["recomp", "r"]:
               try:
                    print("\nProvide a calorie deficit for your Recomp.")
                    # User enters calorie deficit between -200 and 0:
                    intakenum = int(input("Enter a number between -200 and 0: "))
                    # Display error when the number is less than -200:
                    if intakenum < -200:
                         print("Number must be greater than -200.\n")
                         continue
                    # Display error when the number is greater than 0:
                    elif intakenum > 0:
                         print("Number must be less than 0.\n")
                         continue
               # If number is not an integer:
               except ValueError:
                    print("Enter a valid number.\n")
               break
          # If goal is lean bulk:
          elif goal in ["lean bulk", "lb"]:
               try:
                    print("\nProvide a calorie surplus for your Lean Bulk.")
                    # User enters calorie surplus between 200 and 450:
                    intakenum = int(input("Enter a number between 200 and 450: "))
                    # Display error when the number is less than 200:
                    if intakenum < 200:
                         print("Number must be greater than 200.\n")
                         continue
                    # Display error when the number is greater than 450:
                    elif intakenum > 450:
                         print("Number must be less than 450.\n")
                         continue
               # If number is not an integer:
               except ValueError:
                    print("Enter a valid number.\n")
               break
          # If goal is dirty bulk:
          elif goal in ["dirty bulk", "db"]:
               try:
                    print("\nProvide a calorie surplus for your Dirty Bulk.")
                    # User enters calorie surplus between 500 and 750:
                    intakenum = int(input("Enter a number between 500 and 800: "))
                    # Display error when the number is less than 500:
                    if intakenum < 500:
                         print("Number must be greater than 500.\n")
                         continue
                    # Display error when the number is greater than 800:
                    elif intakenum > 750:
                         print("Number must be less than 800.\n")
                         continue
               # If number is not an integer:
               except:
                    print("Enter a valid number.\n")
               break
          # If none of the goals are chosen:
          else:
               print("Please enter one of the goals.\n")
          break

     while True:
          # Switches imperial to metric measurement for easier calculations:
          if system in ["imperial","i"]:
               weight_kg = (lbs/2.20462)
               height_cm = (feet*30.48) + (inches*2.54)
          # Keeps kilograms and centimeters if user prefers metric:
          elif system in ["metric","m"]:
               weight_kg = weight_kg
               height_cm = height_cm
          # Display error if imperial or metric were not selected:
          else:
               print("System must be 'Imperial' or 'Metric'.\n")
          break

     while True:
          # If Male, calcualte Basic Metabolism Rate with formula:
          if gender in ["male","m"]:
               bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) + 5
          # If Female, calcualte Basic Metabolism Rate with formula:
          elif gender in ["female","f"]:
               bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) - 161
          # Display error if male or female were not selected:
          else:
               raise ValueError("Gender must be 'Male' or 'Female'.\n")
          break

     # Displays activity level table and allows user to specify activity level:
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
          activity = input("Enter your activity level (s/l/m/h/i): ").lower()
          # If one of the activity levels are not selected:
          if activity not in ["sedentary", "s", "light", "l", "moderate", "m", "high", "h", "intense", "i"]:
               print("Please provide one of the options in the 'ACTIVITY LEVEL' column.\n")
          
          # Define multipliers for the activity levels:
          activity_factors = {
               "sedentary": 1.15,
               "s": 1.15,
               "light": 1.36,
               "l": 1.36,
               "moderate": 1.52,
               "m": 1.52,
               "high": 1.71,
               "h": 1.71,
               "intense": 1.87,
               "i": 1.87
               }
          
          # If activity level is not in the activity_factors list, give an error:
          if activity not in activity_factors:
               raise ValueError("Invalid activity level.\n")
          
          # Calculate the Total Daily Expenditure:
          tdee = bmr * activity_factors[activity]
          # Calculate the total calories to display:
          calories = tdee + intakenum
          # Display calories needed based on user's fitness goal:
          print(f"\n\nDAILY REQUIREMENTS:\nCalories: {calories:,.0f} kcal")


          # Asks if user wants to calculate again, if not then end program:  
          calculate_again = input("\nWould you like to calculate again? (y/n): ").lower()
          # Re-run program if yes:
          if calculate_again in ["yes", "y"]:
               calculate_calories()
          # Quit if no:
          elif calculate_again in ["no", "n"]:
               print("Thanks for playing!\n")
               break
          # If neither option is entered:
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     calculate_calories()
