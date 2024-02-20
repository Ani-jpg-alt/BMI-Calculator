import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert height from cm to meters
    bmi = weight / (height ** 2)
    interpretation = interpret_bmi(bmi)
    result_label.config(text=f"Your BMI is: {bmi:.2f}\nYou are classified as: {interpretation}")

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Create input labels and entry fields
weight_label = ttk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
weight_entry = ttk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = ttk.Label(root, text="Height (cm):")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
height_entry = ttk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Create button to calculate BMI
calculate_button = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create label to display result
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()