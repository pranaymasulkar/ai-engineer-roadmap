name ="Pranay Masulkar"
age = 32
experience = 7

print(f"My name is {name}, and i have {experience} years of experience. and i am {age} year old.")


# datq types

strintype = "Pranay"
intigerType = 30
floatType = 30.5
booleanType = True
noneType = None
listType = [30,34,54]
tupleType = (12,32,43)
dictionaryType ={"name": "pranay", "age": 30}
settype ={1,2,3}

print(f"these are defferant types in python. string - {strintype}, Intiger - {intigerType}, Float - {floatType}, Boolean - {booleanType}, None - {noneType}, list - {listType}, tuple - {tupleType}, dictionary - {dictionaryType}, set - {settype}")

# Type of in Python

print(type(strintype), type(intigerType), type(floatType), type(booleanType), type(noneType), type(listType), type(tupleType), type(dictionaryType), type(settype))

years = "32"

print(type(years))

print(type(int(years)))

# Assignment

student = {
    "name": "Pranay Masulkar",
    "age": 32,
    "city":"tumsar",
    "percentage":67,
    "course_name": "Python + Js",
    "enrolled" : True
}

print(student)
print(student["name"])
print(student["age"])
print(student["city"])
print(student["percentage"])
print(student["course_name"])
print(student["enrolled"])


# Basic aclculation in python

a = 23
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)

# Type conversion

price = "1500"
quantity = "3"

print(int(price)*int(quantity))