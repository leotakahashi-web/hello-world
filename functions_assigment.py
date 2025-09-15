import math

# Function 1: Area of a Circle
def area_of_circle(pi, radius):
    return round(pi * radius ** 2, 2)

# Function 2: Total Due (money + tax)
def total_due(money, tax_rate):
    return round(money + (money * tax_rate), 2)

# Function 3: Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * (5/9), 5)


# ---------------------------
# Main Program with Input
# ---------------------------
# Test Area of a Circle
radius = float(input("Enter radius of circle: "))
print("Area of circle:", area_of_circle(math.pi, radius))

# Test Total Due
money = float(input("Enter amount of money: "))
tax_rate = float(input("Enter tax rate (as decimal, e.g., 0.06 for 6%): "))
print("Total due:", total_due(money, tax_rate))

# Test Temperature Conversion
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print("Celsius:", fahrenheit_to_celsius(fahrenheit))
