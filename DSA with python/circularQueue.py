import array as array
class Queue:
    def __init__(self,size):
        self.front=-1
        self.rear=-1
        self.arr=array.array('i', [0]*size)
    def isEmpty(self):
        return self.front==-1
    def isFull(self):
        return (self.front==0 and self.rear==self.size()-1 or(self.front==self.rear+1))
    def enqueue(self,item):
        if self.rear==-1:
            self.front=self.rear=0
        elif self.rear==self.size()-1:
            self.rear=0
        else:
            self.rear+=1
        self.arr[self.rear]=item
    def dequeue(self):
        temp=self.arr[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        elif self.front==self.size()-1:
            self.front=0
        else:
            self.front+=1
        return temp
    def peek(self):
        return self.arr[self.front]
    def size(self):
        return len(self.arr)
    def display(self):
        print("------"*self.size()+"-")
        if(q.front<=q.rear):
            print("|    "*(self.front),end="")
            for i in range(self.front,self.rear+1):
                print('|',format(self.arr[i],'>3'),end=" ")
            print("|    "*(self.size()-(self.rear+1)),end="")
        else:
            for i in range(0,self.rear+1):
                print('|',format(self.arr[i],'>3'),end=" ")
            print("|    "*(self.front-(self.rear+1)),end="")
            for i in range(self.front,self.size()):
                print('|',format(self.arr[i],'>3'),end=" ")
        print("|")
        print("------"*self.size()+"-")
size=int(input("Enter the size of the queue:"))
q=Queue(size)
while (True): 
    print("\nPROGRAM TO IMPLEMENT CIRCULAR QUEUE") 
    print("==============================") 
    print("\tl. Enqueue") 
    print("\t2. Dequeue") 
    print("\t3. Peek") 
    print("\t4. Display") 
    print("\t5. Exit") 
    print("===============================") 
    choice=int(input("Enter your Choice: ")) 
    if choice==1:
        if q.isFull():
            print("Queue Overflow")
        else:
            num=int(input("Enter the data: "))
            q.enqueue(num)
    elif choice==2:
        if q.isEmpty():
            print("Queue Underflow")
        else:
            num=q.dequeue() 
            print("Item dequeued = ", num) 
    elif choice==3: 
        if q.isEmpty(): 
            print("Queue Underflow") 
        else: 
            num=q.peek() 
            print("Item at the front of the Queue = ", num) 
    elif choice==4 : 
        if q.isEmpty() : 
            print("Queue is Empty") 
        else: 
            q.display() 
    elif choice==5 : 
        print("\nQuiting...") 
        break 
    else: 
        print("Invalid choice. Please Enter Correct Choice") 
        continue