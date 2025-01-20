def Bubble_sort(list,n):
    for i in range(n-1):
        flag=False
        for j in range(n-1-i):
            if list[j]>list[j+1]:
                temp=list[j]  
                list[j]=list[j+1]
                list[j+1]=temp
                flag=True
        if flag==False:
            break
    Print_list(list,n)
def Print_list(list,n):
    for i in range(n):
        print(list[i],end=" ")
n=int(input("Enter the range : "))
list=[]
for i in range(n):
    x=int(input("Enter the number : "))
    list.append(x)
print("Print the list before sorted : ")
for i in range(n):
     print(list[i],end=" ")
print("\nPrint the list after sorted : ")
Bubble_sort(list,n)