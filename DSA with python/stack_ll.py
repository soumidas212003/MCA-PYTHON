class Node: 
    def __init__(self, Newdata, link): 
        self.data = Newdata 
        self.next = link 
class Stack: 
    def __init__(self): 
        self.top = None 
    def isEmpty(self): 
        return self.top is None 
    def peek(self): 
        return self.top.data 
    def pop(self):  
        node=self.top 
        self.top = self.top.next 
        return node.data 
    def push(self, Newdata):  
        self.top = Node (Newdata, self.top) 
    def display(self):  
        curNode = self.top 
        print() 
        while curNode is not None : 
            print('|',format (curNode.data, '>'),' |')
            print("-----------------")
            curNode = curNode.next 
s=Stack() 
while (True): 
    print("\nPROGRAM TO IMPLEMENT STACK") 
    print ("============================") 
    print("\tl. Push") 
    print("\t2. Pop") 
    print("\t3. Peek") 
    print("\t4. Display") 
    print("\t5. Exit") 
    print ("============================")
    choice=int(input("Enter your Choice: ")) 
    if choice==1: 
        num=int(input("Enter the Data: ")) 
        s.push(num) 
    elif choice==2: 
        if s.isEmpty(): 
            print("Stack Underflow") 
        else: 
            num=s.pop(); 
            print("Popped data = ", num) 
    elif choice==3: 
        if s.isEmpty(): 
            print("Stack Underflow") 
        else: 
            num=s.peek() 
            print("data at top of stack = ", num) 
    elif choice==4 : 
        if s.isEmpty(): 
            print("Stack is Empty") 
        else: 
            s.display() 
    elif choice==5: 
        print("\nQuiting.......") 
        break 
    else: 
        print("Invalid Choice Please Enter Correct Choice")
        continue