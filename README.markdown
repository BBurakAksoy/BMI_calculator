# BMI Calculator

This is a simple GUI application built with Python and Tkinter to calculate Body Mass Index (BMI) based on user-provided weight and height.

## Features

- User-friendly interface to input weight (in kg) and height (in cm).
- Calculates BMI and displays the result along with the corresponding health category.
- Includes a "Clear" button to reset the input fields and result.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone the repository or download the `BMI_Calculator.py` file.
2. Ensure Python 3.x is installed on your system.
3. Run the script using the command:
   ```
   python BMI_Calculator.py
   ```

## Usage

1. Launch the application by running the script.
2. Enter your weight in kilograms in the "Enter Your Weight (kg)" field.
3. Enter your height in centimeters in the "Enter Your Height (cm)" field.
4. Click the "Calculate" button to compute your BMI.
5. The result will display your BMI value and health category.
6. Click the "Clear" button to reset the fields and result.

## BMI Categories

The application categorizes BMI values as follows:

- **Severely thin**: BMI ≤ 16
- **Moderately thin**: 16 < BMI ≤ 17
- **Mild thin**: 17 < BMI ≤ 18.5
- **Normal weight**: 18.5 < BMI ≤ 25
- **Overweight**: 25 < BMI ≤ 30
- **Obese class 1**: 30 < BMI ≤ 35
- **Obese class 2**: 35 < BMI ≤ 40
- **Obese class 3**: BMI > 40