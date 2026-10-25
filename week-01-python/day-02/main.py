# string in python
name = "PRANAY Masulkar"
message = "Helow bhai " + name
print(message)
print(message.lower())
print(message.upper())
print(message.title())

quetion = "what      is your     name       ?"
print(quetion.strip())

# Replace text

text = "i am learning java"

print(text.replace("java","Python"))

#Check whether text contains a word

text2 = "Exaplin artificial inteligence"

print("inteligence" in text2)

# String formatting with f-strings

user = "Pranay"
email = "pranay@gmail.com"

print(f"user name is {user} and email id is {email}.")

# Type conversion in Python 

ages = input("Enter Your Age : ")
ageconvert = int(ages)
print(ageconvert + 1)

num = str(input("Enter any number: "))
print(num + "the number.")

boolnum = input("Enter your value: ")
print(bool(boolnum))

# Examle

price = float(input("Enter product price: "))
quantity = int(input("enter quantity: "))
totalprice = price * quantity

print(totalprice)


# Operators in Python

a = int(input("Enter first number :"))
b = int(input("Enter second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# comparson opernator

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)


# logical operator

score = int(input("Enter scrore : "))
completed = True

if score >= 100 and completed:
    print("You win the game.")
else:
    print("You loss the game.")


# taking input from user.

userName = input("Enter your name : ")
userSkill = input("Enter which technology you are learning?:  ")
print(f"Hello, {userName}")
print(f"you are lenaning {userSkill}.")
print(f"{userName} keep practicing everyday and master these skills {userSkill}.")