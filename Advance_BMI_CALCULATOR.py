import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
import csv

# Store user data
users_data = []

def calculate_bmi():
    try:
        # Get user inputs
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validate inputs
        if not name:
            messagebox.showerror("Invalid Input", "Name cannot be empty!")
            return
        if weight <= 0 or weight > 500:
            messagebox.showerror("Invalid Input", "Weight must be greater than 0 and less than 500 kg!")
            return
        if height <= 0 or height > 3:
            messagebox.showerror("Invalid Input", "Height must be greater than 0 and less than 3 meters!")
            return

        # Calculate BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        # Categorize BMI
        if bmi < 18.5:
            category = "Underweight"
            tip = "Consider eating nutrient-rich foods, increasing caloric intake, and consulting a healthcare provider."
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
            tip = "Maintain a balanced diet and regular physical activity to stay healthy."
        elif 25 <= bmi < 30:
            category = "Overweight"
            tip = "Focus on a balanced diet, portion control, and regular physical activity. Seek advice if needed."
        else:
            category = "Obesity"
            tip = "Adopt a calorie-controlled diet and regular physical activity. Seek medical advice for a structured plan."

        # Add to user data
        user_data = {"Name": name, "BMI": bmi, "Category": category, "Tip": tip}
        users_data.append(user_data)

        # Update listbox
        user_listbox.insert(tk.END, f"{name}: BMI = {bmi}, Category = {category}, Tip: {tip[:50]}...")

        # Reset input fields
        name_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height!")

def save_results():
    if not users_data:
        messagebox.showinfo("No Data", "No user data to save!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "BMI", "Category", "Tip"])
            writer.writeheader()
            writer.writerows(users_data)
        messagebox.showinfo("Save Successful", f"Results saved to {file_path}")

def show_graph():
    if not users_data:
        messagebox.showinfo("No Data", "No user data to display!")
        return

    names = [user["Name"] for user in users_data]
    bmis = [user["BMI"] for user in users_data]

    plt.figure(figsize=(10, 5))
    plt.bar(names, bmis, color="skyblue", alpha=0.7)
    plt.axhline(y=18.5, color="green", linestyle="--", label="Normal weight lower bound (18.5)")
    plt.axhline(y=25, color="orange", linestyle="--", label="Overweight lower bound (25)")
    plt.axhline(y=30, color="red", linestyle="--", label="Obesity lower bound (30)")

    plt.xlabel("Users")
    plt.ylabel("BMI")
    plt.title("BMI Comparison for Users")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Create main Tkinter window
root = tk.Tk()
root.title("Multi-User BMI Calculator with Health Tips")
root.geometry("600x500")

# Input fields
tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Weight (kg):", font=("Arial", 12)).pack(pady=5)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

tk.Label(root, text="Height (m):", font=("Arial", 12)).pack(pady=5)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Buttons
calculate_button = tk.Button(root, text="Add BMI", font=("Arial", 12), command=calculate_bmi)
calculate_button.pack(pady=10)

save_button = tk.Button(root, text="Save Results", font=("Arial", 12), command=save_results)
save_button.pack(pady=5)

graph_button = tk.Button(root, text="Show Graph", font=("Arial", 12), command=show_graph)
graph_button.pack(pady=5)

# User list
tk.Label(root, text="Users' BMI Results (with Health Tips):", font=("Arial", 12)).pack(pady=5)
user_listbox = tk.Listbox(root, font=("Arial", 12), width=80, height=10)
user_listbox.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
