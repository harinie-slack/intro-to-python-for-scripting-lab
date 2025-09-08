# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    # define variable to take input for a letter
    letter = input("Enter a letter (a-z) or (A-Z): ")
    # define a list of vowels 
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    if letter in vowels:
        print("The letter" ,letter, "is a vowel")
    else:
        print("The letter" ,letter, "is a consonant")

# Call the function
check_letter()

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    # define var to take input for users age and convert to int
    age = int(input("Please enter your age: "))
    # define var to rep voting age
    voting_age = 18
    # determining if user is voting age
    if age >= voting_age:
        print("You are eligible to vote!")
    else:
        print("Sorry, you cannot vote right now.")

# Call the function
check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = int(input("Input a dog's age: "))
    if dog_age > 2:
        # def var if dog is older than 2
        dog_years = (20 + ((dog_age - 2) * 7))
        print("The dog's age in dog years is" ,dog_years)
    elif dog_age == 2:
        print("The dog's age in dog years is 20")
    elif dog_age == 1:
        print("The dog's age in dog years is 10")

# Call the function
calculate_dog_years()

# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    # defining vars to capture yes or no for cold and rain
    is_cold = input("Is it cold? (yes/no) ")
    is_raining = input("is it raining? (yes/no) ")

    # defining stmnts for various combos of yes and no to above qs
    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")

# Call the function
weather_advice()

# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    # getting input for month and day
    month = input("Enter the month of the year using the first three letters with the first letter capitalized (Jan - Dec): ")
    day = int(input("Enter the day of the month: "))
    # creating list of months and possible days
    ls_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days_30 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    days_31 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    days_29 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

    # determining what season the month and day belong to
    if month == ls_months[0] and day in days_31:
            print(month, day, "is in Winter")
    elif month == ls_months[1] and day in days_29:
        print(month, day, "is in Winter")
    elif month == ls_months[2] and (day >=1 and day <= 19):
        print(month, day, "is in Winter")
        if day >= 20:
            print(month, day, "is in Spring")
    elif month == ls_months[3] and day in days_30:
        print(month, day, "is in Spring")
    elif month == ls_months[4] and day in days_31:
        print(month, day, "is in Spring")
    elif month == ls_months[5] and (day >=1 and day <=20):
        print(month, day, "is in Spring")
        if day >= 21:
            print(month, day, "is in Summer")
    elif month == ls_months[6] and day in days_31:
        print(month, day, "is in Summer")
    elif month == ls_months[7] and day in days_31:
        print(month, day, "is in Summer")
    elif month == ls_months[8] and (day >= 1 and day <= 21):
        print(month, day, "is in Summer")
        if day >= 22:
            print(month, day, "is in Fall")
    elif month == ls_months[9] and day in days_31:
        print(month, day, "is in Fall")
    elif month == ls_months[10] and day in days_30:
        print(month, day, "is in Fall")
    elif month == ls_months[11] and (day >=1 and day <=20):
        print(month, day, "is in Fall")
        if day >= 21:
            print(month, day, "is in Winter")


# Call the function
determine_season()



