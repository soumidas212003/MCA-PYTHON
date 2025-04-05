class stack:
    def __init__(self):
        self.mylist=[]
    def isempty(self):
        return len(self.mylist)==0
    def push(self,val):
        self.mylist.append(val)
    def pop(self):
        return self.mylist.pop()
    def peek(self):
        return self.mylist[-1]
    # def display(self):
    #     print(self.mylist)   
    def display(self):
        top=len(self.mylist)-1
        print()
        for i in range(top,-1,-1):
            print('|',format(self.mylist[i],'>3'),'|')
            print("--------")
s=stack()
while(True):
    print("\nProgram To Implement Stack....")
    print("\t1.Push")
    print("\t2.Pop")
    print("\t3.Peek")
    print("\t4.Display")
    print("\t5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        num=int(input("Enter the Data: "))
        s.push(num)
    elif ch==2:
        if s.isempty():
            print("Stack Underflow")
        else:
            num=s.pop()
            print("Popped item = ",num)
    elif ch==3:
        if s.isempty():
            print("Stack Underflow")
        else:
            num=s.peek()
            print("Item at top of stack = ",num)
    elif ch==4:
        if s.isempty():
            print("Stack is Empty")
        else:
            s.display()
    elif ch==5:
        print("\nQuiting....")
        break
    else:
        print("Invalid choice.. please Enter Correct Choice")
        continue