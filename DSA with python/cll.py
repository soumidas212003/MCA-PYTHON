class Node:
    def __init__(self,mydata=None,mylink=None):
        self.data=mydata
        self.next=mylink
class CLL:
    def __init__(self):
        self.head=None
    def insert_beg(self,mydata):
        newnode=Node(mydata)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
        else:
            curnode=self.head
            while curnode.next is not self.head:
                curnode=curnode.next
            newnode.next=self.head
            curnode.next=newnode
            self.head=newnode
    def insert_end(self,mydata):
        newnode=Node(mydata)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
        else:
            curnode=self.head
            while curnode.next is not self.head:
                curnode=curnode.next
            newnode.next=self.head
            curnode.next=newnode
    def display(self):
        if self.head is None:
            print("Empty list..")
        else:
            curnode=self.head
            while curnode.next is not self.head:
                print(curnode.data,end="->")
                curnode=curnode.next
            print(curnode.data)
    def delete_first(self):
        if self.head is None:
            print("Empty list Deletion not Possible")
        else:
            curnode=self.head
            if curnode.next==curnode:
                self.head=None
                del(curnode)
            else:
                while curnode.next is not self.head:
                    curnode=curnode.next
                self.head=self.head.next
                del(curnode.next)
                curnode.next=self.head
            print("Node Deleted successfully...")
    def delete_end(self):
        if self.head is None:
            print("Empty list Deletion not Possible")
        else:
            curnode=self.head
            if curnode.next==curnode:
                self.head=None
                del(curnode)
            else:
                while curnode.next.next is not self.head:
                    curnode=curnode.next
                del(curnode.next)
                curnode.next=self.head
            print("Node Deleted successfully...")
    def insert_nth(self,mydata,posn):
        newnode=Node(mydata)
        if self.head is None:
            self.head=newnode
            newnode.next=newnode
        elif posn==1:
            curnode=self.head
            while curnode.next is not self.head:
                curnode=curnode.next
            curnode.next=newnode
            newnode.next=self.head
            self.head=newnode
        else:
            curnode=self.head
            i=1
            while i<=posn-2 and curnode.next is not self.head:
                curnode=curnode.next
                i+=1
            newnode.next=curnode.next
            curnode.next=newnode
    
        curnode=self.head
        if self.head is None:
            print("Empty list ...Deletion not possible...")
        elif posn==1:
            self.head=curnode.next
            del(curnode)
        else:
            i=1
            while i<=posn-2 and curnode.next is not None:
                curnode=curnode.next
                i+=1
            if curnode.next is None:
                print("Node not found..")
            else:
                temp=curnode.next
                curnode.next=temp.next
                del(temp)  
    
list1=CLL()
list1.insert_beg(10)
list1.display()
list1.insert_end(20)
list1.display()
list1.delete_first()
list1.display()
list1.insert_end(40)
list1.display()
list1.delete_end()
list1.display()
list1.insert_nth(5,5)
list1.display()
list1.insert_nth(5,1)
list1.display()