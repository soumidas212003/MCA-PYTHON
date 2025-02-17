def insertionsort(mylist):
    length=len(mylist)
    for i in range(1,length):
        n=mylist[i]
        j=i-1
        while j>=0 and mylist[j]>n:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=n
    return mylist
a=[]
n=int(input("How many number we take: "))
for i in range(n):
    element=int(input("Enter the number: "))
    a.append(element)
result=insertionsort(a)
print("The sorted list is: ",result)