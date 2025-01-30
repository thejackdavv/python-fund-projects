# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workouts.append(workout_type + " " + duration)


def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories.append(calories_consumed)


def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_workout_time = 0
    sum_calories = 0
    for element in workouts:
        element = element.split()
        total_workout_time += int(element[1])
    for element in calories:
        sum_calories += int(element)
    print(f"Your total workout time is: {total_workout_time} minutes")
    print(f"Your total calories intake is: {sum_calories} calories")



def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    pass


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    pass


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    pass


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration

            workout = input("Enter the type of your workout: ")
            duration_of_workout = input("Enter the duration in minutes: ")
            log_workout(workout, duration_of_workout)


        elif choice == '2':
            # Prompt for calories consumed
            calorie_intake = input("Enter the amount of calories: ")
            log_calorie_intake(calorie_intake)


        elif choice == '3':
            # Call view_progress function
            view_progress()

            pass
        elif choice == '4':
            # Call reset_progress function
            pass
        elif choice == '5':
            # Prompt for daily goals
            pass
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()