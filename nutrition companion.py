user_data = {}
food_log = {}


def is_number(text):

    if text == "":
        return False

    dot_count = 0
    valid_chars = "0123456789."

    for char in text:
        is_valid_char = False
        for vc in valid_chars:
            if char == vc:
                is_valid_char = True

        if is_valid_char == False:
            return False

        if char == ".":
            dot_count = dot_count + 1

    if dot_count > 1:
        return False

    return True


def get_valid_input(prompt):

    value = -1.0
    valid = False

    while valid == False:
        user_input = input(prompt)
        if is_number(user_input):
            value = float(user_input)
            if value > 0:
                valid = True
            else:
                print("Please enter a number greater than 0.")
        else:
            print('That does not look like a valid number. Try again.')

    return value


def update_profile():
    global user_data
    print("\n-- Let's Get to Know You ---")

    name = input("First things first, what should I call you? ")

    weight = get_valid_input('How much do you weigh right noww (in kg)? ')
    height = get_valid_input("And how tall are you (in cm)? ")
    age = int(get_valid_input("How young are you (years)? "))

    gender = ""
    while gender != "m" and gender != "f":
        gender = input("What is your biological sex? (M/F): ").strip().lower()

    print("\nHow active are you usually?")
    print("1. Sedentary (office job, little exercise)")
    print("2. Lightly Active (1-3 days/week)")
    print("3. Moderately Active (3-5 days/week)")
    print("4. Very Active (6-7 days/week)")
    print("5. Extra Active (physical job)")

    choice = "0"
    multiplier = 1.2

    valid_choice = False
    while valid_choice == False:
        choice = input('Which number best describes you? (1-5): ')
        if choice == "1":
            multiplier = 1.2
            valid_choice = True
        elif choice == "2":
            multiplier = 1.375
            valid_choice = True
        elif choice == '3':
            multiplier = 1.55
            valid_choice = True
        elif choice == "4":
            multiplier = 1.725
            valid_choice = True
        elif choice == "5":
            multiplier = 1.9
            valid_choice = True
        else:
            print("Please choose 1, 2, 3, 4, or 5.")

    user_data = {
        "name": name,
        "weight": weight,
        "height": height,
        "age": age,
        "gender": gender,
        "activity_multiplier": multiplier
    }

    print("\nProfile updated!")
    calculate_metrics()


def calculate_metrics():
    if user_data == {}:
        print("I don't have your details yet. Please update your proofile first!")
    else:
        name = user_data['name']
        w = user_data['weight']
        h = user_data['height']
        a = user_data['age']
        g = user_data['gender']
        act = user_data['activity_multiplier']

        # BMI Logic
        height_m = h / 100
        bmi = w / (height_m * height_m)

        bmi_category = ""
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 25:
            bmi_category = "Normal weight"
        elif bmi < 30:
            bmi_category = 'Overweight'
        else:
            bmi_category = "Obese"


        bmr = 0
        if g == 'm':
            bmr = (10 * w) + (6.25 * h) - (5 * a) + 5
        else:
            bmr = (10 * w) + (6.25 * h) - (5 * a) - 161

        tdee = bmr * act

        print("\n--- " + name + "'s Health Insights ---")
        print("Your BMI is " + str(round(bmi, 1)) + " (" + bmi_category + ")")
        print("Maintenance Calories: " + str(int(tdee)) + " per day")
        print("To Lose Weight: " + str(int(tdee - 500)))


def log_food():

    today = "Current Session"


    if today not in food_log:
        food_log[today] = []

    print("\n--- Log Food ---")
    food_name = input("Food item name: ")
    calories = get_valid_input("Calories: ")
    protein = get_valid_input('Protein (g): ')

    entry = {
        "food": food_name,
        "calories": calories,
        "protein": protein
    }

    food_log[today].append(entry)

    print("Logged!")


def view_log():
    print("\n--- Your Food Diary ----")
    if food_log == {}:
        print("No logs yet.")
    else:

        dates = []
        for d in food_log:
            dates.append(d)


        n = len(dates)
        for i in range(n):
            for j in range(0, n - i - 1):
                if dates[j] < dates[j + 1]:
                    # Swap
                    temp = dates[j]
                    dates[j] = dates[j + 1]
                    dates[j + 1] = temp

        for date in dates:
            entries = food_log[date]


            total_cals = 0
            total_prot = 0
            for e in entries:
                total_cals = total_cals + e['calories']
                total_prot = total_prot + e['protein']

            print("\nDate: " + date + " | Total: " + str(int(total_cals)) + " kcal")
            for entry in entries:
                print(" - " + entry['food'] + ": " + str(int(entry['calories'])) + " kcal")


def main():

    print("\n✨ Nutrition Companion ✨")

    running = True
    while running:
        if "name" in user_data:
            print("\nHello " + user_data["name"])

        print("1. Update Profile")
        print("2. Check Goals")
        print("3. Log Food")
        print("4. View History")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == '1':
            update_profile()
        elif choice == '2':
            calculate_metrics()
        elif choice == "3":
            log_food()
        elif choice == "4":
            view_log()
        elif choice == "5":
            print('Goodbye! (Note: Data is not saved in this version)')
            running = False
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
