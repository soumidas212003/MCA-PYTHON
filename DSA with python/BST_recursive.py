class Node:
    def __init__(self,newData=None,lchild=None,rchild=None):
        self.left=lchild
        self.data=newData
        self.right=rchild
def insert_rec(root,mydata):
    if root is None:
        return Node(mydata)
    elif mydata<root.data:
        root.left=insert_rec(root.left,mydata)
    else:
        root.right=insert_rec(root.right,mydata)
    return root
def preorder(root):
    if root is not None:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')
def search(curNode,key):
    if curNode is None or curNode.data== key:
        return curNode
    elif key<curNode.data:
        return search(curNode.left, key)
    else:
        return search(curNode.right, key)
def findLargest(curNode):
    if curNode is None or curNode.right is None:
        return curNode
    else:
        return findLargest(curNode.right)
def findSmallest(curNode):
    if curNode is None or curNode.left is None:
        return curNode
    else:
        return findSmallest(curNode.left)
def countNode(curnode):
    if curnode is None:
        return 0
    else:
        return countNode(curnode.left)+countNode(curnode.right)+1
def findHeight(curnode):
    if curnode is None:
        return 0
    else:
        heightleft=findHeight(curnode.left)
        heightright=findHeight(curnode.right)
        if heightleft>heightright:
            return heightleft+1
        else:
            return heightright+1
bst=None
while True:
    print("\nProgram to Implement binary search tree")
    print("\t1.Insert Node")
    print("\t2.Preorder traversal")
    print("\t3.Inorder traversal")
    print("\t4.Postorder traversal")
    print("\t5.Search an element")
    print("\t6.Find largest Node")
    print("\t7.Find smallest Node")
    print("\t8.Count total number of Node")
    print("\t9.Determine the height of the tree")
    print("\t10.Exit")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        num=int(input("Enter the Data: "))
        bst=insert_rec(bst,num)
    elif ch == 2:
        print("PreOrder: ",end=' ')
        preorder(bst)
    elif ch == 3:
        print("InOrder: ",end=' ')
        inorder(bst)
    elif ch == 4:
        print("PostOrder: ",end=' ')
        postorder(bst)
    elif ch == 5:
        num=int(input("Enter the data you want to search: "))
        findNode=search(bst,num)
        if findNode is None:
            print("Node not found")
        else:
            print("Node found")
    elif ch == 6:
        if bst is None:
            print("Null tree")
        else:
            max=findLargest(bst)
            print("Largest element: ",max.data)
    elif ch == 7:
        if bst is None:
            print("Null tree")
        else:
            min=findSmallest(bst)
            print("Smallest element: ",min.data)  
    elif ch == 8:
        c=countNode(bst)
        print("Total number of Nodes",c)
    elif ch == 9:
        h=findHeight(bst)
        print("Height of the tree: ",h)
    elif ch == 10:
        print("\nQuiting.....")
        break
    else:
        print("Invalid choice...Please Enter Correct Choice")
        continue      