# Practice Deciding what I want eat Using Python
# This will use my caloric maintenance level - my desired caloric deficit
# Curernt Maintenance level is 3256
# Calories deficit is 726
OPTIONS = ["EATOUT", "MAKE_SOMETHING", "STARVE"]
# Assume Chic Fil A is the healthiest and Pizza is the worst
EATOUT = ["CHIC FIL A", "KOREAN FOOD", "PIZZA"]
# Assume "Chicken Wings" is the healthiest and "Banging Steak" the worst
MAKE_SOMETHING = ["MAKE CHICKEN WINGS", "MAKE TRADITIONAL FOOD", "MAKE A BANGING STEAK"]
STARVE = ["REMEMBER YOUR CALORIE DEFICIT"]
WORK_OUT_TYPE = ["PUSH", "PULL", "LEGS", "REST"]
PUSH = ["CHEST","TRICEPS","SHOULDER"]
PULL = ["BACK","BICEPS","FOREARMS"]
LEGS = ["GLUTES", "QUADS", "HAMSTRINGS", "CALVES"]
Daily_Caloric_Maintenance = 2500
def Calculate_Calories():
    Calories_Burned = input("How many calories did you burn today? ")
    Calories_Burned = -int(Calories_Burned)
    DEFICIT = Daily_Caloric_Maintenance + Calories_Burned
    if DEFICIT >= 2500:
        print("You did not Burn enough caloreis")
        if DEFICIT >= 2800 and DEFICIT < 2999:
            print(STARVE)
            print('Go run for 30 mins')
            What_Type_of_Workout()
            return
        elif DEFICIT >= 3000:
            print('Go to the gym')
            print('Go run for 30 mins')
            What_Type_of_Workout()
    elif DEFICIT < 2500 and DEFICIT > 2000:
        print("Burn more calories to treat yourself")
        if DEFICIT <= 2499 and DEFICIT >= 2350:
            print("Only Get The Chicken Thighs800")
            print(MAKE_SOMETHING[0])
            What_Type_of_Workout()
        elif DEFICIT <= 2349 and DEFICIT >= 2200:
            print("You Can Treat Yourself With A Steak")
            print(MAKE_SOMETHING[2])
            What_Type_of_Workout()
        else:
            print("Finally You Can Learn How To Cook")
            print(MAKE_SOMETHING[1])
            What_Type_of_Workout()
    else:
        print("You can treat yourself")
        if DEFICIT <= 2000 and DEFICIT >= 1750:
            print(EATOUT[0])
        elif DEFICIT <= 1749 and DEFICIT >= 1500:
            print(EATOUT[1])
        else:
            print(EATOUT[2])
def What_Type_of_Workout():
    Workout_Type = input('What work out day is it? ').upper().rstrip()
    if Workout_Type not in WORK_OUT_TYPE:
        What_Type_of_Workout()
    if Workout_Type == "PUSH":
        print("Pick 2 Below")
        print("Chest/Triceps/Shoulder")
        Types_Of_Exercies_PUSH()
        Types_Of_Exercies_PUSH()
    elif Workout_Type == "PULL":
        print("Pick 2 Below")
        print("Back/Biceps/Forearms")
        Types_Of_Exercies_PULL()
        Types_Of_Exercies_PULL()
    elif Workout_Type == "LEGS":
        print("Pick 3 Below")
        print("Quads/Adducts/Hamstrings/Calves")
        print("Do Not Forget Calves")
        Types_Of_Exercies_LEGS()
        Types_Of_Exercies_LEGS()
        Types_Of_Exercies_LEGS()
    elif Workout_Type == "REST":
        print('You can relax!')
def Types_Of_Exercies_PUSH():
    Exercise = input('What do you want to work out? ').upper().rstrip()
    if Exercise not in PUSH:
        Types_Of_Exercies_PUSH()
    if Exercise == "CHEST":
        print('Pick 3')
        print("Barbell Bench Press", "Dumbbell Bench Press", "Chest Press", "Chest Flys", "Cable Crossovers", "Barbell Pullovers")
    elif Exercise == "TRICEPS":
        print('Pick 3')
        print("Cable Pulldown", "Skull Crusher", "Laying Triceps Extention", "Overhead Triceps Extention")
    else:
        print('Pick 3')
        print["Shoulder Press", "Front Raises", "Face Pulls", "Lateral Raises", "Front Raises"]
def Types_Of_Exercies_PULL():
    Exercise = input('What do you want to work out? ').upper().rstrip()
    if Exercise not in PULL:
        Types_Of_Exercies_PULL()
    if Exercise == "BACK":
        print('Pick 3')
        print("Cable Row", "Pulldowns", "ISO-Lateral Highrow", "Dumbbell Row", "T-Bar Row")
    elif Exercise == "BICEPS":
        print('Pick 3')
        print("Preacher Curls", "Dumbbell Curls", "Cable-Curls", "Hammer Curls", "Barbell Curls")
    else:
        print('Pick 3')
        print("Forearm Barbell Curls", "Wrist Curls")
def Types_Of_Exercies_LEGS():
    Exercise = input('What do you want to work out? ').upper().rstrip()
    if Exercise not in LEGS:
        Types_Of_Exercies_LEGS()
    if Exercise == "QUADS":
        print('Pick 2')
        print("Leg Extenstions", "Hacksquat", "Dumbbell Squats")
    elif Exercise == "HAMSTRING":
        print('Pick 2')
        print("Leg Press", "Leg Curl", "RDL")
    elif Exercise == "Adducts":
        print('Pick 2')
        print("Squats", "Adductor Machine")
    else:
        print('Pick 2')  
        print("Calves Press", "Weighted Calve Raises", "Seated Car Raises")
def main():
    print('Are you hungry today Feranmi?')
    Calculate_Calories()
main()