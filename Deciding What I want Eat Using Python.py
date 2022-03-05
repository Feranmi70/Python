# Practice Deciding what I want eat Using Python
# This will use my caloric maintenance level - my desired caloric deficit
# Curernt Maintenance level is 3256
# Calories deficit is 726
OPTIONS = ["EATOUT", "MAKE_SOMETHING", "STARVE"]
EATOUT = ["CHIC FIL A", "KOREAN FOOD", "PIZZA"]
MAKE_SOMETHING = ["MAKE CHICKEN WINGS", "MAKE TRADITIONAL FOOD", "MAKE A BANGING STEAK"]
STARVE = ["REMEMBER YOUR CALORIE DEFICIT"]
WORK_OUT_TYPE = ["PUSH", "PULL", "LEGS", "REST"]
PUSH = ["CHEST","TRICEPS","SHOULDER"]
PULL = ["BACK","BICEPS","FOREARMS"]
LEGS = ["GLUTES", "QUADS", "HAMSTRINGS", "CALVES"]
Daily_Caloric_Maintenance = 2500
def Calculate_Calories():
    Calories_Burned = input("How many calories did you burn today? ")
    Calories_Burned = int(Calories_Burned)
    DEFICIT = Daily_Caloric_Maintenance + Calories_Burned
    if DEFICIT >= 2500:
        print("You did not Burn enough caloreis")
        if DEFICIT >= 2800 and DEFICIT < 2999:
            print(STARVE)
            print('Go run for 30 mins')
            return
        elif DEFICIT >= 3000:
            print('Go to the gym')
            print('Go run for 30 mins')
            What_Type_of_Workout()
    elif DEFICIT < 2500 and DEFICIT > 2000:
        print("Burn more calories to treat yourself")
        if DEFICIT <= 2499 and DEFICIT >= 2350:
            print(MAKE_SOMETHING[0])
        elif DEFICIT <= 2349 and DEFICIT >= 2200:
            print(MAKE_SOMETHING[2])
        else:
            print(MAKE_SOMETHING[1])
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
    if Workout_Type == "PUSH":
        print("Pick 2 Below")
        print("Chest/Triceps/Shoulder")
        Types_Of_Exercies_PUSH()
    elif Workout_Type == "PULL":
        print("Pick 2 Below")
        print("Back/Biceps/Forearms")
    elif Workout_Type == "LEGS":
        print("Do Not Forget Calves")
    elif Workout_Type == "REST":
        print('You can relax!')
    else:
        Workout_Type = input('Try again ').upper().rstrip()
def Types_Of_Exercies_PUSH():
    Exercise = input('What do you want to work out? ').upper().rstrip()
    if Exercise == "CHEST":
        print('Pick 3')
        print("Barbell Bench Press", "Dumbbell Bench Press", "Chest Press", "Chest Flys", "Cable Crossovers", "Barbell Pullovers")
    elif Exercise == "TRICEPS":
        print('Pick 3')
        print("Cable Pulldown", "Skull Crusher", "Laying Triceps Extention", "Overhead Triceps Extention")
    else:
        print('Pick 3')
        print["Shoulder Press", "Front Raises", "Face Pulls", "Lateral Raises", "Front Raises"]
def main():
    print('Are you hungry today Feranmi?')
    Calculate_Calories()
main()