class Node:
    def __init__(self,newcoef=None,newpower=None,link=None):
        self.coef=newcoef
        self.pwr=newpower
        self.next=link
class polynomial:
    def __init__(self):
        self.head=None
    def insert_end(self,newcoef,newpower):
        newnode=Node(newcoef,newpower)
        if self.head is None:
            self.head=newnode
        else:
            curnode=self.head
            while curnode.next is not None:
                curnode=curnode.next
            curnode.next=newnode
    def create_poly(self):
        while True:
            cof=int(input("Enter coefficient: "))
            pr=int(input("Enter power: "))
            self.insert_end(cof,pr)
            ch=input("Continue? (y/n): ")
            if ch.upper()=='N':
                break
    def display(self):
        if self.head is None:
            print("Empty list...")
        else:
            curnode=self.head
            while curnode is not None:
                print(str(curnode.coef)+"x^"+str(curnode.pwr),end=" + ")
                curnode=curnode.next
            print("\b\b ")
    def add_poly(p1,p2):
        poly1=p1.head
        poly2=p2.head
        poly3=polynomial()
        while poly1 is not None and poly2 is not None:
            if poly1.pwr > poly2.pwr:
                poly3.insert_end(poly1.coef,poly1.pwr)
                poly1=poly1.next
            elif poly1.pwr < poly2.pwr:
                poly3.insert_end(poly2.coef,poly2.pwr)
                poly2=poly2.next
            else:
                poly3.insert_end(poly1.coef+poly2.coef,poly1.pwr)
                poly1=poly1.next
                poly2=poly2.next
        while poly1 is not None:
            poly3.insert_end(poly1.coef,poly1.pwr)
            poly1=poly1.next
        while poly2 is not None:
            poly3.insert_end(poly2.coef,poly2.pwr)
            poly2=poly2.next
        return poly3
pol1=polynomial()
pol2=polynomial()
print("Enter value for 1st polynomial:- ")
pol1.create_poly()
pol1.display()
print("Enter value for 2nd polynomial:- ")
pol2.create_poly()
pol2.display()
pol3=polynomial.add_poly(pol1,pol2)
print("sum is: ",end="")
pol3.display()