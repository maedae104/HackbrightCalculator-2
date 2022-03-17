"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,power, mod, add_mult, add_cubes)
result = 0
while True:
    #take in user input indefinitely 
    user_input = input("Enter your equation. > ")

    #split/tokenize user input
    tokens = user_input.split(" ")
    
    operator = tokens[0]
    
    
    # num1 = tokens[1]
    # num2 = tokens[2]

    num1 = float(tokens[1])
    num2 = float(tokens[2])
    
    #unless "q" inputted
    if user_input == 'q' or user_input == 'quit':
        break

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
    elif len(tokens) < 3:
        num3 = "0"

    elif len(tokens) > 3:
        num3 = float(tokens[3])

    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)

    elif operator == "/":
        result = divide(num1, num2)

    elif operator == "%":
        result = mod(num1, num2)

    elif operator == "**":
        result = power(num1, num2)

    elif operator == "square":
        result = square(num1)

    elif operator == "cube":
        result = cube(num1)

    elif operator == "add_mult":
        result = add_mult(num1, num2, num3)

    elif operator == "add_cubes":
        result = add_cubes(num1, num2, num3)
   
    #based on user input calculate run math function
    
    # else:
    #     result = "Please enter an operator followed by two integers."

    print(result)
# Replace this with your code
