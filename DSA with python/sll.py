class Node:
    def __init__(self,mydata=None,mylink=None):
        self.data=mydata
        self.next=mylink
class SLL:
    def __init__(self):
        self.head=None
    def insert_beg(self,mydata):
        newnode=Node(mydata)
        newnode.next=self.head
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
    def delete_end(self):
        if self.head is None:
            print("Empty list..Deletion not possible...")
        elif self.head.next is None:
            del(self.head)
            self.head=None
        else:
            curnode=self.head
            while curnode.next.next is not None:
                curnode=curnode.next
            del(curnode.next)
            curnode.next=None
    def insert_nth(self,mydata,posn):
        newnode=Node(mydata)
        if self.head is None:
            self.head=newnode
        elif posn==1:
            newnode.next=self.head
            self.head=newnode
        else:
            curnode=self.head
            i=1
            while i<=posn-2 and curnode.next is not None:
                curnode=curnode.next
                i+=1
            newnode.next=curnode.next
            curnode.next=newnode
    def delete_nth(self,posn):
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
    def count(self):
        curnode=self.head
        c=0
        while curnode is not None:
            c+=1
            curnode=curnode.next
        return c
    def largestnode(self):
        maxnode=curnode=self.head
        while curnode is not None:
            if curnode.data>maxnode.data:
                maxnode=curnode
            curnode=curnode.next
        return maxnode
    def reverse(self):
        curnode=self.head
        nextnode=curnode.next
        prevnode=None
        curnode.next=None
        while nextnode is not None:
            prevnode=curnode
            curnode=nextnode
            nextnode=curnode.next
            curnode.next=prevnode
        self.head=curnode

list1=SLL()

list1.insert_beg(5)
list1.display()
list1.insert_beg(6)
list1.display()
list1.insert_end(10)
list1.display()
list1.insert_nth(4,3)
list1.display()
list1.delete_end()
list1.display()
list1.delete_first()
list1.display()
list1.delete_nth(2)
list1.display()
list1.insert_beg(6)
list1.display()
list1.insert_end(10)
list1.display()
list1.delete_nth(5)
list1.display()
c=list1.count()
print("Number of Nodes:",c)
l=(list1.largestnode()).data
print("largest node's data =",l)
list1.reverse()
list1.display()
