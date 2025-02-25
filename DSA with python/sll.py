class Node:
    def __init__(self,mydata=None,mylink=None):
        self.data=mydata
        self.next=mylink
class SLL:
    def __init__(self):
        self.head=None
    def insert_beg(self,mydata):
        newnode=Node(mydata,self.head)
        self.head=newnode
    def insert_end(self,mydata):
        newnode=Node(mydata)
        if self.head==None:
            self.head=newnode
        else:
            curnode=self.head
            while curnode.next is not None:
                curnode=curnode.next
            curnode.next=newnode
    def display(self):
        curnode=self.head
        while curnode is not None:
            print(curnode.data,end="->")
            curnode=curnode.next
        print("None")
    def delete_first(self):
        tempnode=self.head
        if self.head is None:
            print("Null list Deletion not Possible")
        else:
            self.head=tempnode.next
            del(tempnode)
    def node_sorted(self, mydata):
        temp = Node(mydata)
        # If the list is empty or the new node should be the new head
        if self.head is None or self.head.data > mydata:
            temp.next = self.head
            self.head = temp
            return
        # Traverse the list to find the correct position
        h2 = self.head
        while h2.next is not None and h2.next.data < mydata:
            h2 = h2.next
        # Insert the node
        temp.next = h2.next
        h2.next = temp
list1=SLL()
list1.insert_beg(10)
list1.insert_beg(20)
list1.insert_beg(30)
list1.insert_beg(40)
list1.insert_end(50)
list1.delete_first()
list1.display()
list1.node_sorted(5)
list1.display()