import matplotlib.pyplot as plt
import csv

def calculate_bmi():
    try:
        # Input weight
        weight_unit = input("Enter the unit of your weight (kg for kilograms, lb for pounds): ").lower()
        if weight_unit == "kg":
            weight = float(input("Enter your weight in kilograms (kg): "))
        elif weight_unit == "lb":
            weight = float(input("Enter your weight in pounds (lb): "))
            weight *= 0.453592  # Convert pounds to kilograms
        else:
            print("Invalid weight unit entered!")
            return

        # Validate weight range
        if weight <= 0 or weight > 500:
            print("Weight must be greater than 0 and less than 500 kg!")
            return

        # Input height
        height_unit = input("Enter the unit of your height (m for meters, cm for centimeters, ft for feet/inches): ").lower()
        if height_unit == "m":
            height = float(input("Enter your height in meters (m): "))
        elif height_unit == "cm":
            height = float(input("Enter your height in centimeters (cm): "))
            height /= 100  # Convert centimeters to meters
        elif height_unit == "ft":
            feet = float(input("Enter your height in feet: "))
            inches = float(input("Enter additional inches: "))
            height = (feet * 0.3048) + (inches * 0.0254)  # Convert feet and inches to meters
        else:
            print("Invalid height unit entered!")
            return

        # Validate height range
        if height <= 0 or height > 3:
            print("Height must be greater than 0 and less than 3 meters!")
            return

        # Calculate BMI
        BMI = weight / (height ** 2)

        # Categorize BMI
        if BMI < 18.5:
            category = "Underweight"
            tip = "Consider eating nutrient-rich foods, increasing caloric intake, and consulting a healthcare provider."
        elif 18.5 <= BMI < 25:
            category = "Normal weight"
            tip = "Maintain a balanced diet and regular physical activity to stay healthy."
        elif 25 <= BMI < 30:
            category = "Overweight"
            tip = "Focus on a balanced diet, portion control, and regular physical activity. Seek advice if needed."
        else:
            category = "Obesity"
            tip = "Adopt a calorie-controlled diet and regular physical activity. Seek medical advice for a structured plan."

        # Display results
        print(f"\nYour BMI is: {round(BMI, 2)}")
        print(f"Category: {category}")
        print(f"Health Tip: {tip}")

        # Save results to a file
        save_results(round(BMI, 2), category, tip)

        # Graphical representation
        show_graph(round(BMI, 2))
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def save_results(bmi, category, tip):
    # Save results to a text file
    with open("bmi_result.txt", "w") as txt_file:
        txt_file.write(f"BMI Result:\n")
        txt_file.write(f"BMI: {bmi}\n")
        txt_file.write(f"Category: {category}\n")
        txt_file.write(f"Health Tip: {tip}\n")
    print("Results saved to bmi_result.txt")

    # Save results to a CSV file
    with open("bmi_result.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["BMI", "Category", "Tip"])
        csv_writer.writerow([bmi, category, tip])
    print("Results saved to bmi_result.csv")

def show_graph(bmi):
    categories = ["Underweight", "Normal weight", "Overweight", "Obesity"]
    thresholds = [18.5, 25, 30]

    # Prepare data for graph
    category_bmis = [18.5, 25, 30, bmi]
    colors = ["blue", "green", "orange", "red"]

    plt.bar(categories, category_bmis, color=colors, alpha=0.6, label="BMI Ranges")
    plt.axhline(y=bmi, color="purple", linestyle="--", label=f"Your BMI ({bmi})")

    plt.xlabel("Categories")
    plt.ylabel("BMI Values")
    plt.title("Your BMI vs. Standard BMI Ranges")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Run the program
calculate_bmi()
