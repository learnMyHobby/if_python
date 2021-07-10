# Write a python program to check whether a character is uppercase or lowercase alphabet.

character = input("Enter the character: ")

if(character.isupper()):
    print(f"{character} is an uppercase alphabet")
elif(character.islower()):
    print(f"{character} is an lowercase alphabet")
else:
    print(f"The entered character is not an alphabet ")

