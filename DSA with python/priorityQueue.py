class Node:
    def __init__(self,newData,newPr=5):
        self.data=newData
        self.pr=newPr
class priorityQueue:
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def enqueue(self,newData,newPr=5):
        newitem=Node(newData,newPr)
        rear=len(self.item)
        for i in range(rear):
            if newitem.pr>self.item[i].pr:
                self.item.insert(i,newitem)
                break
        else:
            self.item.append(newitem)
    def dequeue(self):
        return self.item.pop(0)
    def peek(self):
        return self.item[0]
    def display(self):
        for i in self.item:
            print('(',i.data,',',i.pr,')',end=',')
        print()
    def size(self):
        return len(self.item)
pq=priorityQueue()
while(True):
    print("\nPROGRAM TO IMPLEMENT PRIORITY QUEUE")
    print("====================================")
    print("\t1.Enqueue")
    print("\t2.Dequeue")
    print("\t3.Peek")
    print("\t4.Size")
    print("\t5.Display")
    print("\t6.Exit")
    print("====================================")
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        num=int(input("Enter Your Data: "))
        pr=input("Enter Priority Value: ")
        if pr == "":
            pq.enqueue(num)
        else:
            pq.enqueue(num,int(pr))
        #pq.enqueue(num,pr)
    elif ch==2:
        if pq.isEmpty():
            print("Queue UnderFlow")
        else:
            popNode=pq.dequeue()
            print("Item dequeued = ",popNode.data," With Priority ",popNode.pr)
    elif ch==3:
        if pq.isEmpty():
            print("Queue UnderFlow")
        else:
            popNode=pq.peek()
            print("Item at the front of the queue = ",popNode.data," With Priority ",popNode.pr)
    elif ch==4:
        if pq.isEmpty():
            print("Queue is Empty")
        else:
            size=pq.size()
            print("Size is : ",size)
    elif ch==5:
        if pq.isEmpty():
            print("Queue is Empty")
        else:
            pq.display()
    elif ch==6:
        print("\nQuiting....")
        break
    else:
        print("Invalid Choice....Please enter correct choice")
        continue