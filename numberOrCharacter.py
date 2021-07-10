#  WAP to find whether given input is number or character.

character = input("Enter the character: ")

if(character.isalpha()):
    print(f"The entered character {character} is alphabet")
elif(character.isalnum()):
    print(f"The entered character is {character} which is a number ")
else:
    print("It is neither character nor number")