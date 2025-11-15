num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

# print(f"The result is ${result}.")
match operation:
    case "+":
       result =  int(num1 + num2)
    case "-":
       result =  int(num1 - num2)
    case "*":
       result = int(num1 * num2)
    case "/":
      if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
      result =  int(num1 / num2)
    case _:
      print("invalid Operation")
      exit()
      
print(f"The result is {result}.")
