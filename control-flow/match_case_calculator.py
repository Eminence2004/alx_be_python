num1 = input("Enter first number: ")

num2 = input("Enter second number: ")

operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        result = float(num1) + float(num2)

    case "-":
        result = float(num1) - float(num2)

    case "*":
        result = float(num1) * float(num2)

    case "/":
        if float(num2) != 0:    
            result = float(num1) / float(num2)  
        else:
            result = "Error: Cannot divide by zero."

    case _:
        result = "Error: Invalid operation."
print(f"The result is: {result}")