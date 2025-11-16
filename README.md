# The problem statment

<img width="1135" height="348" alt="image" src="https://github.com/user-attachments/assets/9502537c-567f-4dd3-a508-9c6013dafbe2" />

# 📐 Quadratic Equation Root Calculator

A simple command-line Python script to calculate the real roots of a quadratic equation in the form ax2+bx+c=0.

# ✨ Features

- User Input: Prompts the user to enter the coefficients a, b, and c.
- Root Calculation: Applies the quadratic formula to determine the two roots, r1 and r2
- Formatted Output: Prints the calculated roots, formatted to four significant figures.

# 📝 Usage

When you run the script, it will prompt you to enter the three coefficients:

    Enter a =

    Enter b =

    Enter c =

The script will then output the two calculated roots:

    One root is r1 = -2.0
    Another root is r2 = -3.0

⚠️ Important Note: This script does not include error handling for the discriminant (b2−4ac). If the discriminant is negative, the roots are complex (imaginary), and the script will throw a ValueError because it attempts to take the square root of a negative number.


