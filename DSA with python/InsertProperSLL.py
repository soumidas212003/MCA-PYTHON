class Node:
    def __init__(self,mydata=None,mylink=None):
        self.data=mydata
        self.next=mylink
class SLL:
    def __init__(self):
         self.head=None
    def insert_proper(self,mydata):
            newnode=Node(mydata)
            if self.head is None:
                self.head=newnode
            elif mydata<self.head.data:
                newnode.next=self.head
                self.head=newnode
            else:
                curnode=self.head
                while curnode is not None and mydata>curnode.data:
                    prev=curnode
                    curnode=curnode.next
                newnode.next=prev.next
                prev.next=newnode
    def display(self):
            curnode=self.head
            while curnode is not None:
                print(curnode.data,end="->")
                curnode=curnode.next
            print("None")
list1=SLL()
list1.insert_proper(5)
list1.insert_proper(1)
list1.insert_proper(10)
list1.insert_proper(2)
list1.display()