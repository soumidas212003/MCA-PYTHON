class Stack:
    def __init__(self):
        self.mylist=[]
    def isempty(self):
        return len(self.mylist)==0
    def push(self,val):
        self.mylist.append(val)
    def pop(self):
        return self.mylist.pop()
    def peek(self):
        return self.mylist[-1]
class Node:
    def __init__(self,newData=None,lchild=None,rchild=None):
        self.left=lchild
        self.data=newData
        self.right=rchild
class BST:
    def __init__(self):
        self.root=None
    def insert(self,newData):
        newNode=Node(newData)
        if self.root is None:
            self.root=newNode
        else:
            curNode=self.root
            parent=None
            while curNode is not None:
                parent=curNode
                if newData<curNode.data:
                    curNode=curNode.left
                else:
                    curNode=curNode.right
            if newData<parent.data:
                parent.left=newNode
            else:
                parent.right=newNode
    def preOrder(self):
        st=Stack()
        st.push(None)
        curNode=self.root
        while curNode is not None:
            print(curNode.data,end=" ")
            if curNode.right:
                st.push(curNode.right)
            if curNode.left:
                curNode=curNode.left
            else:
                curNode=st.pop()
    def inOrder(self):
        st=Stack()
        st.push(None)
        curNode=self.root
        while curNode is not None:
            while curNode is not None:
                st.push(curNode)
                curNode=curNode.left
            curNode=st.pop()
            flag=True
            while curNode and flag is True:
                print(curNode.data, end=" ")
                if curNode.right:
                    curNode=curNode.right
                    flag=False
                else:
                    curNode=st.pop()
    def search(self,key):
        curNode=self.root
        while curNode is not None:
            if key == curNode.data:
                return curNode
            elif key < curNode.data:
                curNode = curNode.left
            else:
                curNode = curNode.right
        return curNode
    def findLargest(self):
        largestNode=self.root
        while largestNode.right is not None:
            largestNode=largestNode.right
        return largestNode
    def findSmallest(self):
        smallestNode=self.root
        while smallestNode.right is not None:
            smallestNode=smallestNode.left
        return smallestNode
bst=BST()
while True:
    print("\nProgram to Implement binary search tree")
    print("\t1.Insert Node")
    print("\t2.Preorder traversal")
    print("\t3.Inorder traversal")
    print("\t4.Search an element")
    print("\t5.Find largest Node")
    print("\t6.Find smallest Node")
    print("\t7.Exit")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        num=int(input("Enter the Data: "))
        bst.insert(num)
    elif ch == 2:
        print("PreOrder: ",end=' ')
        bst.preOrder()
    elif ch == 3:
        print("InOrder: ",end=' ')
        bst.inOrder()
    elif ch == 4:
        num=int(input("Enter the data you want to search: "))
        findNode=bst.search(num)
        if findNode is None:
            print("Node not found")
        else:
            print("Node found")
    elif ch == 5:
        if bst is None:
            print("Null tree")
        else:
            max=bst.findLargest()
            print("Largest element: ",max.data)
    elif ch == 6:
        if bst is None:
            print("Null tree")
        else:
            min=bst.findSmallest()
            print("Smallest element: ",min.data)  
    elif ch == 7:
        print("\nQuiting.....")
        break
    else:
        print("Invalid choice...Please Enter Correct Choice")
        continue      