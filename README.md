🥗 Nutrition Companion

A "Zero-Dependency" Health Tracker built in Pure Python.

Nutrition Companion is  application designed to help you track your health metrics and food intake.

The Unique Twist: This project was built entirely from scratch without importing any external libraries or standard modules (like math, pandas, or datetime). Every algorithm—from sorting logs to calculating complex metabolic formulas—is manually implemented using raw logic.

⚡ Key Features

📊 Instant Health Metrics

BMI Calculator: Calculates Body Mass Index and categorizes it (Underweight, Normal, Overweight, Obese).

BMR & TDEE: Uses the Mifflin-St Jeor Equation to determine exactly how many calories you burn at rest and during your daily activities.

🍎 Food Logging

Track individual food items with specific calorie and protein values.

Maintain a running log of your current session.

📜 History Viewer

View a chronological history of your logged items.

Uses a custom-written Bubble Sort algorithm to organize data.

🛡️ Robust Validation

Includes a custom input parser that validates numbers character-by-character, ensuring the app never crashes on bad input.

🚀 How to Run

Since this project uses no external dependencies, running it is incredibly simple.

Prerequisites: Ensure you have Python installed on your computer.

Download: Save the script as nutrition.py.

Run: Open your terminal or command prompt and execute:

python nutrition.py


🛠️ Under the Hood

Because we didn't use import, we had to get creative. Here is how the core tech works:

1. The Validation Engine (is_number)

Instead of using try/except ValueError, we built a state machine that iterates through input strings. It checks against a whitelist of valid characters (0-9 and .) and ensures only one decimal point exists per number.

2. The Sorting Engine (Bubble Sort)

To keep the food log organized, we implemented a manual sorting algorithm:

for i in range(n):
    for j in range(0, n - i - 1):
        if dates[j] > dates[j + 1]:
             # Manual Swap
             temp = dates[j]
             dates[j] = dates[j + 1]
             dates[j + 1] = temp


3. The Math

We use raw arithmetic for all health formulas. For example, the BMR calculation logic:

Men: (10 * weight) + (6.25 * height) - (5 * age) + 5

Women: (10 * weight) + (6.25 * height) - (5 * age) - 161

⚠️ Important Note on Data

This application uses Runtime Memory. Because we do not use file handling libraries (like json or sqlite3), your data is not saved after you close the program. This tool is designed for quick, single-session checks or educational purposes.
