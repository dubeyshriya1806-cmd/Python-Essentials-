Multi-Utility Unit Converter
📖 Overview of the Project
The Multi-Utility Unit Converter is a menu-driven Python application designed to streamline everyday unit conversion tasks.

In academic and professional settings, converting between Metric and Imperial systems (e.g., Kilometers to Miles) is a frequent requirement. Manual calculation is time-consuming and prone to human error. This project solves that problem by providing a centralized, accurate, and user-friendly tool that handles calculations for Weight, Length, Volume, and Temperature instantly.

✨ Features
Category-Based Selection: Users can choose from four distinct measurement categories.
Bidirectional Conversion: Supports conversion both ways (e.g., C to F and F to C).
Error Handling: Uses try-except blocks to catch invalid inputs (like typing text instead of numbers) without crashing the program.
Continuous Execution: Uses a while loop so users can perform multiple conversions without restarting the program.
Decimal Precision: Automatically rounds results to 2 decimal places for readability.
🛠 Technologies & Tools Used
Programming Language: Python 3.14
Libraries: Standard Python Libraries (sys implied, no external pip installation required).
IDE/Editor: VS Code
Concepts Applied:
Modular Programming (Functions)
Conditional Logic (if-elif-else)
Looping Structures (while)
Exception Handling (try-except)
⚙️ Steps to Install & Run
Since this project uses standard Python libraries, no external dependencies are needed.

Prerequisites: Ensure you have Python installed on your system. You can check this by typing:

python --version
Installation: Download the file Multi-Utility Converter.py to your local machine.

Running the Project: Open your terminal (Command Prompt or Terminal), navigate to the folder containing the file, and run:

Multi-Utility Converter.py
🧪 Instructions for Testing
Follow these steps to verify the accuracy of the program:

Scenario 1: Weight Conversion

Run the program.
Select Option 1 (Weight).
Select Option 1 (Kg to Lbs).
Input Value: 50.
Expected Output: Result: 50.0 kg = 110.23 lbs.
Scenario 2: Volume Conversion

Select Option 3 (Volume).
Select Option 2 (Gallons to Liters).
Input Value: 10.
Expected Output: Result: 10.0 Gallons = 37.85 Liters.
Scenario 3: Invalid Input Handling

Select any category.
When asked for a value, type hello and press Enter.
Expected Output: Error: Please enter a valid number. (The program should not crash).
📸 Screenshots
Note: All the screenshots are provided in screenshots.md.
