# day-01 pythn fundamentals

name = "Pranay Masulkar"
experience = "7 years"
learnig_ai = True

print("Hello,", name)
print("Years of development experience", experience)
print("Learning GEnrative AI", learnig_ai)

# Basic calculatinons

javascript_projects = 50
python_projects = 1
total_project = javascript_projects + python_projects

print("Total Projects", total_project)

# A simple function in python

def introduce(name, goal):
    return f"My name is {name}. My goal is to become a {goal}"

message = introduce("Pranay Masulkar", "Genrative AI Engineer.")
print(message)


# Variaables And Data types

address = "tumsar"  # Strin
age = 32                # Intiger
height = 5.8            # Float
having_mobile = True    # Boolean

print(f"My name is {name} and i am from {address}, and i am {age} year old, height is {height} and i have iphone is - {having_mobile}.")


# List and Dictionaries

skills = ["HTML", "CSS", "javascript", "typescript", "nodeJs", "NexttJs", "MongoDb", "Python"]

devloper = {
    "name": "Pranay Masulkar",
    "role":"Frontend Engineer",
    "Skil": skills
}

print(devloper["role"])
print(devloper["Skil"])
print(devloper["Skil"][3])

# Functions

def calculate_total(a, b):
    return a + b
result = calculate_total(10, 30)
print(result)

# A small exercise related to AI

data = ["react", "python", "mongodb", "node.js"]

def format_skills(data):
     # Return each skill in title case
    return [item.title() for item in data]
pass

formated = format_skills(data)
print(formated)