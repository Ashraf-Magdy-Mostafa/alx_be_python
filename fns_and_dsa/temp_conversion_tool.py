
FAHRENHEIT_TO_CELSIUS_FACTOR = ""
CELSIUS_TO_FAHRENHEIT_FACTOR = ""

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)
def convert_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32


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
                print(f"{temp} is {convert_to_celsius(temp)}")
            case "c":
                print(f"{temp} is {convert_to_fahrenheit(temp)}")
            case _:
                print("Error: Invalid unit specified. Please enter 'C' or 'F'.")









if __name__ == "__main__":
    main()