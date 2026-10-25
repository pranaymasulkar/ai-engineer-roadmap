# Day 2 Ai promp Builder

print("== AI promp builder ==")

name =  input("Enter your name: ").strip()
topic = input("What do you want to learn? :").strip()
level = input("Your Level (beginner/intermediate/advanced): ").strip().lower()


if not name or not topic:
    print("Error: Name and topic can not be empty.")

elif level not in ["beginner","intermediate","advanced)"]:
    print("Error: please enter the valid learning level.")

else:
    prompt = f"Act as a programing tutor for {name}. Exaplin {topic} at a{level} level Use simple examples, practical exercises, and explain the code step by step."

    print("\n === genrated prompt ===")

    print(prompt)

    print("\n === prompt length ", len(prompt), "charedtor" )


# Exercise 1: String manipulation
# Ask the user for a sentence, remove extra spaces, and print it in uppercase.

sen = input("Enter your thought: ").strip()
print(sen.upper())

# Exercise 2: Calculate a total
# Ask for a product price and quantity, convert them to numbers, and calculate the total.

askprice = int(input("What is price of product: "))
askquanti = int(input("How many quantity: "))

total_ask_price = askprice * askquanti
print(total_ask_price)

# Exercise 4: Input validation
# Update the mini project so the learning level accepts Beginner, INTERMEDIATE, and other capitalization variations.

