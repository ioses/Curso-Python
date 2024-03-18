from bonus.parsers14 import parse
from bonus.converters14 import convert



feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result=convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result<1:
    print("kid is too small")
else:
    print("Kid is correct")