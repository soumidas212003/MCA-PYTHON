#1+2+4+7+11+16...UPTO N TERMS
n=int(input("Enter a number: "))
f=1
s=0
r=0
while(r<n):
    f=f+r #1 2 4 7 11
    print(f,"+")
    s=s+f #1 3 7 14 25
    r=r+1
print("sum",s)
