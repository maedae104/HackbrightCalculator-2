"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    #take in user input indefinitely 
    user_input = input("Enter your equation. > ")
     #split/tokenize user input
    tokens = user_input.split(" ")
    operator = tokens[0]
    result = None
    num1 = tokens[1]
    num2 = tokens[2]
    num3 = tokens[3]
    #unless "q" inputted
    if user_input == "q" or "quit":
        break

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue

    elif operator == "+":
        add(num1, num2)

    elif operator == "-":
        subtract(num1, num2)

    elif operator == "*":
        multiply(num1, num2)

    elif operator == "/":
        divide(num1, num2)

    elif operator == "%":
        mod(num1, num2)

    elif operator == "**":
        power(num1, num2)

    elif operator == "square":
        square(num1)

    elif operator == "cube":
        cube(num1)

    elif operator == "add_mult":
        add_mult(num1, num2, num3)

    elif operator == "%":
        add(num1, num2)
   
    #based on user input calculate run math function


# Replace this with your code
