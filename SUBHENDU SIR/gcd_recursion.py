#gcd(Recursion)
def gcd (num1,num2):
    rem=num1%num2
    if rem == 0:
        return num2
    else:
        return gcd(num2,rem)
num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))
print("GCD of",num1,"and",num2,"is",gcd(num1,num2))