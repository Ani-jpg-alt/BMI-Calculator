def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in centimeters.
    Formula: BMI = weight (kg) / ((height (cm) / 100) ** 2)
    """
    bmi = weight / ((height / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value according to standard categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Input weight in kilograms
    weight = float(input("Enter your weight in kilograms: "))

    # Input height in centimeters
    height = float(input("Enter your height in centimeters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    interpretation = interpret_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {interpretation}")

if __name__ == "__main__":
    main()
