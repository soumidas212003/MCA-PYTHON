'''
Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''

def swap_case(s):
    x=""
    for c in s:
        if c.isupper():
            c=c.lower()
        else:
            c=c.upper()  
        x+="".join(c)      
    return x
s=input()
result = swap_case(s)
print(result)