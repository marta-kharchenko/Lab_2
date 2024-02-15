# Part 2
# a) Find the circumference and area of a circle
import math
Radius = input("Please enter the radius of yhe circle: ")
Circumference = 2 * math.pi * float(Radius)
Area = math.pi * float(Radius)**2
print("The circumference of the circle is:", Circumference)
print("The area of the circle is:", Area)

# b) Convert temperatures from Fahrenheit to Celsius
Fahrenheit = input("Please enter the temperature in Fahrenheit: ")
Celsius = (float(Fahrenheit)-32)*5/9
print("The temperature in Celsius is:", Celsius)

# c) Solve a given quadratic equation. e.g. a = 1, b = 3, c = 4
a = 1
b = 3
c = 4
Discriminant = b**2 - 4*a*c
Root_1 = (-b + Discriminant**0.5)/(2*a)
Root_2 = (-b - Discriminant**0.5)/(2*a)
print("The Roots of the equation are:", Root_1, ",", Root_2)

# d) Determine the compound interest
Principal = 5000
APR = 3
n = 10
Amount = Principal * ((1 + APR/100)**n)
print("The Amount is:", Amount)