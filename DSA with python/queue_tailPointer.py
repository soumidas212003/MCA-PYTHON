#Using a single circular linkedlist with a single Tail Pointer
class Node : 
    def __init__(self, Newdata, link ): 
        self.data = Newdata 
        self.next = link
class Queue: 
    def __init__( self ):
        self.tail=None
    def isEmpty(self):
        return self.tail is None
    def enqueue(self, Newdata):
        newNode=Node(Newdata, None)
        if self.tail is None:
            newNode.next = newNode
        else:
            newNode.next=self.tail.next
            self.tail.next= newNode
        self.tail = newNode
    def peek(self):
        return self.tail.next.data
    def dequeue(self):
        frontNode=self.tail.next
        if frontNode.next==frontNode:
            self.tail = None
        else:
            self.tail.next=frontNode.next
        return frontNode.data
    def display (self):
        curNode = self.tail.next
        print() 
        while curNode is not self.tail: 
            print(curNode.data,'->',end="") 
            curNode = curNode.next 
        print(curNode.data)

q=Queue()
while (True):
    print("\nPROGRAM TO IMPLEMENT QUEUE") 
    print("==============================") 
    print("\tl. Enqueue") 
    print("\t2. Dequeue") 
    print("\t3. Peek") 
    print("\t4. Display") 
    print("\t5. Exit") 
    print("===============================") 
    choice=int(input("Enter your Choice: ")) 
    if choice==1: 
        num=int(input("Enter the Data: ")) 
        q.enqueue (num) 
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