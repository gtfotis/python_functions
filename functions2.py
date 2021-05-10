def makeUpper(some_text):
    return some_text.upper()
user_input = input("Type a word of your choice: ")
uppercaseText = makeUpper(user_input)
print("Uppercase version of user input: " + uppercaseText)