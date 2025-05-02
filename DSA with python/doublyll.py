class DNode:
    def __init__(self, Newdata=None, plink=None, nlink=None):
        self.data = Newdata
        self.previous = plink
        self.next = nlink


class doublyLinkedList:
    def __init__(self):
        self.Head = None

    def insert_end(self, Newdata):
        newNode = DNode(Newdata)
        if self.Head is None:
            self.Head = newNode
        else:
            curNode = self.Head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = newNode
            newNode.previous = curNode
    def insert_begin(self, newdata):
        newNode = DNode(newdata,None,self.Head)
        if self.Head is not None:
            self.Head.previous = newNode
        self.Head=newNode
    def insert_before_nth(self, Newdata, location): 
        newNode = DNode(Newdata)
        curNode = self.Head
        if location == 1:
            newNode.next=self.Head
            if self.Head is not None:
                self.Head.previous=newNode
            self.Head=newNode
        else:
            c = 1
            while c <= location-2 and curNode.next is not None:
                c += 1
                curNode = curNode.next
            newNode.previous=curNode
            newNode.next=curNode.next
            if curNode.next != None:
                curNode.next.previous=newNode
            curNode.next=newNode 
    def delete_first(self):
        if self.Head is None:
            print("Empty List. Deletion not possible..")
        else:
            curNode = self.Head
            self.Head =self.Head.next
            if self.Head is not None:
                self.Head.previous = None
            del(curNode)
            print("Node Deleted Successfully...")
    def delete_last(self):
        if self.Head is None:
            print("Empty List. Deletion not possible..")
        elif self.Head.next is None:
            del(self.Head)
            self.Head=None
        else:
            curNode = self.Head
            while curNode.next.next is not None:
                    curNode = curNode.next
            del(curNode.next)
            curNode.next=None
            print("Node Deleted Successfully...")
    def delete_nth(self, posn):
        if self.Head is None:
            print("Empty List. Deletion not possible..")
        else:
            curNode = self.Head
            if posn == 1:
                self.Head = curNode.next
                del(curNode)
                if self.Head is not None:
                    self.Head.previous=None
                print("Node Deleted Successfully...")
            else:
                c = 1
                while c <= posn - 2 and curNode.next is not None:
                    c += 1
                    curNode = curNode.next
                if curNode.next is None:
                    print("Node not found...")
                else:
                    temp = curNode.next
                    curNode.next = temp.next
                    if temp.next is not None:
                        temp.next.previous = curNode
                    del(temp)
                    print("Node Deleted Successfully...")
    def display(self):
        if self.Head is None:
            print("Empty List.")
        else:
            curNode = self.Head
            print("None<=>", end="")
            while curNode is not None:
                print(curNode.data, end="<=>")
                curNode = curNode.next
            print("None")

    def rev_display(self):
        if self.Head is None:
            print("Empty List.")
        else:
            curNode = self.Head
            print("None<=>", end="")
            while curNode.next is not None:
                curNode = curNode.next
            while curNode is not None:
                print(curNode.data, end="<=>")
                curNode = curNode.previous
            print("None")


# Main Program
dll = doublyLinkedList()
while True:
    print("\nPROGRAM TO IMPLEMENT DOUBLY LINKED LIST")
    print("========================================")
    print("1. Create / Append The List")
    print("2. Insert Node At Beginning")
    print("3. Insert Node at Nth Position")
    print("4. Delete First Node")
    print("5. Delete Last Node")
    print("6. Delete Nth Node")
    print("7. Displaying the List")
    print("8. Displaying the List in Reverse Order")
    print("9. Exit")
    print("========================================")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        opt = 'Y'
        while opt.upper() == 'Y':
            num = int(input("Enter the Data: "))
            dll.insert_end(num)
            opt = input("Enter more (y/n): ")
    elif choice == 2:
        num = int(input("Enter the Data: "))
        dll.insert_begin(num)
    elif choice == 3:
        loc = int(input("Enter The Node number Before which new node will be inserted: "))
        num = int(input("Enter the Data: "))
        dll.insert_before_nth(num, loc)
    elif choice == 4:
        dll.delete_first()
    elif choice == 5:
        dll.delete_last()
    elif choice == 6:
        num = int(input("Enter The Node Number You Want To Delete: "))
        dll.delete_nth(num)
    elif choice == 7:
        dll.display()
    elif choice == 8:
        dll.rev_display()
    elif choice == 9:
        print("\nQuitting.......")
        break
    else:
        print("Invalid choice. Please Enter Correct Choice")
        continue
