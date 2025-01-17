#write a python program to determine the character entered by the user is alphabate/ digit/ space.
char=input("Enter a character: ")
if char.isalpha():
    print("The character is an alphabate")
elif char.isspace():
    print("The character is a space")
elif char.isdigit():
    print("The character is a digit")
else:
    print("The character is neither an alphabet, digit, nor space")