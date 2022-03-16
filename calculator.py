"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube, power, mod, add_mult, add_cubes)

while True:
    #take in user input indefinitely 
    user_input = input("Enter your equation. > ")
     #split/tokenize user input
    tokens = user_input.split(" ")
    operator = tokens[0]
    result = None
    num1 = tokens[1]
    num2 = tokens[2]
    
    #unless "q" inputted
    if user_input == "q" or "quit":
        break

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
    elif len(tokens) < 3:
        num3 = "0"

    elif len(tokens) > 3:
        num3 = tokens[3]

    elif operator == "+":
        result = float(add(num1, num2))

    elif operator == "-":
        result = float(subtract(num1, num2))

    elif operator == "*":
        result = float(multiply(num1, num2))

    elif operator == "/":
        result = float(divide(num1, num2))

    elif operator == "%":
        result = float(mod(num1, num2))

    elif operator == "**":
        result = float(power(num1, num2))

    elif operator == "square":
        result = float(square(num1))

    elif operator == "cube":
        result = float(cube(num1))

    elif operator == "add_mult":
        result = float(add_mult(num1, num2, num3))

    elif operator == "add_cubes":
        result = float(add_cubes(num1, num2, num3))
   
    #based on user input calculate run math function

print(result)
# Replace this with your code
