#Write a python program to enter any character if the character is in lowercase, convert it into uppercase and if is in uppercase convert is into lowercase.
char=input("Enter a character: ")
if (char.isalpha and len(char)==1):
    if char.islower():
        print(char.upper())
    else:
        print(char.lower())
else:
    print("Enter character")