# introducing the calculator
print("This calculator takes 2 integers and performs 1 basic calculation")

# defining variables for two integers and operator
num1 = input("Enter your first number: " )
num2 = input("Enter your second number: " )
operator = input("Choose your calculation (+, -, *, /): " )

# adding instructions to operators to perform the calculations
if operator == "+":
    print (int(num1) + int(num2))
elif operator == "-":
     print (int(num1) - int(num2))
elif operator == "*":
      print (int(num1) * int(num2))
elif operator == "/":
      # if denominator = 0, print undefined
      if int(num2) == 0:
           print("Undefined")
      else:
           print (int(num1) / int(num2))
