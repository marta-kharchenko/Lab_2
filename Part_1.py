# Part 1
# a) Find the sum of two number
print("Program to find the sum of two numbers")
Num_1 = input("Please enter your first number: ")
Num_2 = input("Please enter your second number: ")
Summary = float(Num_1) + float(Num_2)
print("The sum is:", Summary)

# b) Swap two variable numbers
print("Program to swap two variables")
Var_1 = input("Please enter your first number: ")
Var_2 = input("Please enter your second number: ")
Var_3 = Var_1
Var_1 = Var_2
Var_2 = Var_3
print("The first variable is:", Var_1)
print("The second variable is:", Var_2)

# c) Calculate the perimeter and area of the rectangle
Width = input("Please enter the width of your rectangle: ")
Length = input("Please enter the length of your rectangle: ")
Perimeter = (float(Width) + float(Length))*2
Area = float(Width)*float(Length)
print("The perimeter of your rectangle is:", Perimeter)
print("The area of your rectangle is:", Area)