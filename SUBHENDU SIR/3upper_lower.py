char=input("Enter a character: ")
if (char.isalpha and len(char)==1):
    if char.islower():
        print(char.upper())
    else:
        print(char.lower())
else:
    print("Enter character")