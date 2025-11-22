
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (FAHRENHEIT_TO_CELSIUS_FACTOR )
def convert_to_fahrenheit(celsius):
    return (celsius * (CELSIUS_TO_FAHRENHEIT_FACTOR)) + 32


def main():
    temp = (input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    try:
        parsed_temp = float(temp)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    match temp_unit:
            case "f":
                print(f"{parsed_temp} is {convert_to_celsius(parsed_temp):.2f}°C")
            case "c":
                print(f"{parsed_temp} is {convert_to_fahrenheit(parsed_temp):.2f}°F")
            case _:
                print("Error: Invalid unit specified. Please enter 'C' or 'F'.")









if __name__ == "__main__":
    main()