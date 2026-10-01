import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils import square, is_even, celsius_to_fahrenheit, greet


name = input("Enter your name: ")
number = float(input("Enter a number: "))


print(greet(name))
print("Square:", square(number))


if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")


print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))