# setup python and run the main.py 

# Create five variables using different data types

name ="Pranay Masulkar" #string
age=32                  #intiger
height = 5.8            #float
having_phone = True     #Boolean
skills  = ["js", "nodejs","typecsript", "react js"]     #list
phone_details ={
    "model":"Iphone 17",
    "storage": 128,
    "colour": "light blue",
    "cameras":"two"
}                               # Dictionaries

print(f"My name is {name}, and i am {age} years old, my height is {height} fit. i have iphone {phone_details["model"], phone_details["storage"], phone_details["colour"]} with {phone_details["cameras"]} setup. its {having_phone} i have iphone.")

# Write a function that adds two numbers

mobile_price = 80000
disscount = 20000

actual_mobile_cost = mobile_price - disscount

print(actual_mobile_cost)

#Write a function that formats a list of skills

def function_skill(skills):
    return [skill.title() for skill in skills]
pass

formated = function_skill(skills)

print(formated)
