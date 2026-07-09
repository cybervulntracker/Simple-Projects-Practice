import re

email = input("Email: ")

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")