# ============================================
# MULTI-UTILITY UNIT CONVERTER
# ============================================

# ---------- Weight Converter ----------
def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms (kg) to Pounds (lbs)")
    print("2. Pounds (lbs) to Kilograms (kg)")

    choice = input("Enter choice (1 or 2): ")

    try:
        weight = float(input("Enter weight value: "))

        if choice == '1':
            result = weight * 2.20462
            print(f"Result: {weight} kg = {round(result, 2)} lbs")

        elif choice == '2':
            result = weight / 2.20462
            print(f"Result: {weight} lbs = {round(result, 2)} kg")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: Please enter a valid number.")


# ---------- Length Converter ----------
def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometers (km) to Miles")
    print("2. Miles to Kilometers (km)")

    choice = input("Enter choice (1 or 2): ")

    try:
        length = float(input("Enter length value: "))

        if choice == '1':
            result = length * 0.621371
            print(f"Result: {length} km = {round(result, 2)} miles")

        elif choice == '2':
            result = length / 0.621371
            print(f"Result: {length} miles = {round(result, 2)} km")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: Please enter a valid number.")


# ---------- Volume Converter ----------
def volume_converter():
    print("\n--- Volume Converter ---")
    print("1. Liters to Gallons (US)")
    print("2. Gallons (US) to Liters")

    choice = input("Enter choice (1 or 2): ")

    try:
        volume = float(input("Enter volume value: "))

        if choice == '1':
            result = volume * 0.264172
            print(f"Result: {volume} Liters = {round(result, 2)} Gallons")

        elif choice == '2':
            result = volume / 0.264172
            print(f"Result: {volume} Gallons = {round(result, 2)} Liters")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: Please enter a valid number.")


# ---------- Temperature Converter ----------
def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter choice (1 or 2): ")

    try:
        temp = float(input("Enter temperature value: "))

        if choice == '1':
            result = (temp * 9/5) + 32
            print(f"Result: {temp}°C = {round(result, 2)}°F")

        elif choice == '2':
            result = (temp - 32) * 5/9
            print(f"Result: {temp}°F = {round(result, 2)}°C")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: Please enter a valid number.")


# ---------- Main Menu ----------
def main():
    while True:
        print("\n===================================")
        print("      MULTI-UTILITY CONVERTER")
        print("===================================")
        print("1. Weight (Kg / Lbs)")
        print("2. Length (Km / Miles)")
        print("3. Volume (Liters / Gallons)")
        print("4. Temperature (°C / °F)")
        print("5. Exit")

        choice = input("Choose a category (1-5): ")

        if choice == '1':
            weight_converter()

        elif choice == '2':
            length_converter()

        elif choice == '3':
            volume_converter()

        elif choice == '4':
            temperature_converter()

        elif choice == '5':
            print("Exiting program. Have a nice day!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


# ---------- Run Program ----------
main()