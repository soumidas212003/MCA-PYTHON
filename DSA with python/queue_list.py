class queue:
    def __init__(self):
        self.mylist=[]
    def isempty(self):
        return len(self.mylist)==0
    def enqueue(self,val):
        self.mylist.append(val)
    def dequeue(self):
        return self.mylist.pop(0)
    def peek(self):
        return self.mylist[0]
    def display(self):
         print(self.mylist)       
q=queue()
while(True):
    print("\nProgram To Implement Stack....")
    print("\t1.Enqueue")
    print("\t2.Dequeue")
    print("\t3.Peek")
    print("\t4.Display")
    print("\t5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        num=int(input("Enter the Data: "))
        q.enqueue(num)
    elif ch==2:
        if q.isempty():
            print("Queue Underflow")
        else:
            num=q.dequeue()
            print("Item dequeued = ",num)
    elif ch==3:
        if q.isempty():
            print("Queue Underflow")
        else:
            num=q.peek()
            print("Item at the front of the queue = ",num)
    elif ch==4:
        if q.isempty():
            print("Queue is Empty")
        else:
            q.display()
    elif ch==5:
        print("\nQuiting....")
        break
    else:
        print("Invalid choice.. please Enter Correct Choice")
        continue