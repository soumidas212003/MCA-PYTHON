#1 10 101 1010 10101 upto n terms
n=int(input("Enter the number: "))
i=1
while(i<=n):
    j=1
    while(j<=i):
        if(j%2==0):
            print(0,end="")
        else:
            print(1,end="")
        j=j+1
    print()
    i=i+1
