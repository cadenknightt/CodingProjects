# Main Calorie Calcualtion function.
def calculate_calories():
     line_break = "\n---------------------------------------------------------------------------------------\n"
     print("\nWelcome to the Calorie Goal Calculator!\n")
     print("I will give you some prompts to fill in and you will\nbe given the essential information for your fitness journey!")
     print (line_break)

     # User enters Gender, Age, and Measurement System
     while True:
          try:
               # Checks if gender is male or female:
               gender = input("Enter your gender (m/f): ").lower()
               if gender not in ["male","m"] and gender not in ["female","f"]:
                    print("Gender must be Male or Female.\n")
                    continue
          except ValueError:
               print("Please provide 'm' for Male or 'f' for Female.\n")
          break
     while True:
          try:
               # Checks if age is 8 or older:
               age = int(input("Enter your age: "))
               if age <= 8:
                    print("Age must be 8 or older.\n")
                    continue
          except ValueError:
               print("Please provide valid number(s).\n")
          break
     while True:
          try:
               # Checks if measurement is imperial or metric:
               system = input("Imperial or Metric system (i/m): ").lower()
               if system not in ["imperial","i","metric","m"]:
                    print("Please enter imperial or metric.\n")
                    continue
          except ValueError:
               print("Please provide 'i' for Imperial or 'm' for Metric.\n")
          break
     print(line_break)
          
     # Enter height and weight that is aligned with selected measurement system.
     while True:
          # If the imperial system was selected, enter feet, inches, and lbs:
          if system in ["imperial","i"]:
               print("Please enter feet, inches, and weight separately.")
               while True:
                    try:
                         feet = int(input("Feet: "))
                         # Checks if feet is between 3 and 8:
                         if feet < 3 and feet > 8:
                              print("Feet must fall within 3 and 8.\n")
                              continue
                    except ValueError:
                         print("Value must be a whole number.\n")
                         continue
                    break
               while True:
                    try:
                         inches = int(input("Inches: "))
                         # Checks if inches are between 0 and 11:
                         if inches < 0 and inches > 11:
                              print("Inches must be between 0 and 11.\n")
                              continue
                    except ValueError:
                         print("Value must be a whole number.\n")
                         continue
                    break
               while True:
                    try:
                         lbs = float(input("Weight in lbs (ex: 160.2): "))
                         # Checks if weight is greater than 0:
                         if lbs <= 0:
                              print("Weight must be greater than 0.\n")
                              continue
                    except ValueError:
                         print("Value must be a whole number.\n")
                         continue
                    break

          # If the metric system was selected, enter centimeters and kilograms:
          elif system in ["metric","m"]:
               print("\nPlease enter centimeters (height) and kilograms (weight) separately.\n")
               while True:
                    try:
                         centimeters = float(int("Centimeters (ex: 184.2): "))
                         # Checks if centimeters are greater than 90:
                         if centimeters < 90:
                              print("Centimeters must be greater than 90.\n")
                              continue
                    except ValueError:
                         print("Value must be a decimal.\n")
                         continue
                    break
               while True:
                    try:
                         kilograms = float(input("Kilograms (ex: 76.7): "))
                         # Checks if kilograms are greater than 0:
                         if kilograms < 0:
                              print("Kilograms must be greater than 0.\n")
                              continue
                    except ValueError:
                         print("Value must be a decimal.\n")
                         continue
                    break

          # Displays workout goal table and allows user to specify workout goal:
          while True:
               print(line_break)
               print("""
     GOAL           |            DESCRIPTION
     -----------------------------------------------------------
     Intense Cut    |       Risk muscle loss, extreme fat loss.
     Slow Cut       |       Preserve muscle, while losing fat.
     Recomp         |       Build muscle, while losing fat.
     Lean Bulk      |       Slow muscle gain, limited fat gain.
     Dirty Bulk     |       Quick muslce and fat gain.
          """)
               goal = input("Enter your goal here (ic/sc/r/lb/db) or full name: ").lower()
               # If goal is intense cut:
               if goal in ["intense cut", "ic"]:
                    while True:
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
                              print("Enter valid numbers.\n")
                              continue
                         break
               # If goal is slow cut:
               elif goal in ["slow cut", "sc"]:
                    while True:
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
                              print("Enter valid numbers.\n")
                              continue
                         break
               # If goal is recomp:
               elif goal in ["recomp", "r"]:
                    while True:
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
                              print("Enter valid numbers.\n")
                              continue
                         break
               # If goal is lean bulk:
               elif goal in ["lean bulk", "lb"]:
                    while True:
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
                              print("Enter valid numbers.\n")
                              continue
                         break
                    # If goal is dirty bulk:
               elif goal in ["dirty bulk", "db"]:
                    while True:
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
                              print("Enter valid numbers.\n")
                              continue
                         break
               # If none of the goals are chosen:
               else:
                    print("Please enter one of the goals.\n")
                    continue
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

          # Define the activity levels and their multipliers once (easy to change later)
          ACTIVITY_MULTIPLIERS = {
               "s":         1.2,
               "sedentary": 1.2,
               "l":         1.38,
               "light":     1.38,
               "m":         1.55,
               "moderate":  1.55,
               "h":         1.75,
               "high":      1.75,
               "i":         1.9, 
               "intense":   1.9,
          }

          # Displays activity level table and allows user to specify activity level:
          while True:
               print(line_break)
               print("""
     ACTIVITY LEVEL   |       DESCRIPTION
     ------------------------------------------------------------
     Sedentary        |       No lifting / little to no exercise
     Light            |       Exercise/sports 1-3 days per week
     Moderate         |       Exercise/sports 3-5 days per week
     High             |       Exercise/sports 6-7 days per week
     Intense          |       Very hard exercise, physical job, or 2x training
               """)

               activity = input("Enter your activity level (s/l/m/h/i or full name): ").lower().strip()
               
               # Checks if input is in Activity Multiplier Dictionarry
               if activity in ACTIVITY_MULTIPLIERS:
                    multiplier = ACTIVITY_MULTIPLIERS[activity]
                    tdee = bmr * multiplier
                    break
               else:
                    print("Invalid choice. Please use one of: s, l, m, h, i or sedentary, light, moderate, high, intense\n")
                    continue

          print(line_break)

          # Calculate total calories
          calories = tdee + intakenum

          # Displays daily needs
          print("DAILY REQUIREMENTS:")
          print(f"Calories: {calories:,.0f} kcal")

          # Asks if user wants to calculate again, if not then end program:  
          print(line_break)
          calculate_again = input("Would you like to calculate again? (y/n): ").lower()
          # Re-run program if yes:
          if calculate_again in ["yes", "y"]:
               calculate_calories()
          # Quit if no:
          elif calculate_again in ["no", "n"]:
               print("Thank you for using my service!\n")
               break
          # If neither option is entered:
          else:
               print("Please enter 'y' for yes or 'n' for no.\n")

if __name__ == "__main__":
     calculate_calories()
