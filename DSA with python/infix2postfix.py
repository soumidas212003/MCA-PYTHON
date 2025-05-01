import string 
class stack: 
    def __init__(self): 
        self.mylist=[] 
    def isempty(self): 
        return len(self.mylist)==0 
    def push (self, val): 
        self.mylist.append(val) 
    def pop (self): 
        return self.mylist.pop() 
    def peek (self): 
        return self.mylist[-1] 
def getPriority(op): 
    if op in "+-": 
        return 1 
    else: 
        return 2 
def infix2postfix (src): 
    st=stack() 
    trgt=''
    for ch in src:
        if ch == '(':
            st.push(ch) 
        elif ch == ')':
            while st.peek() != '(': 
                temp=st.pop() 
                trgt += temp 
            st.pop() 
        elif ch in string.ascii_letters or ch in  string.digits: 
            trgt+=ch 
        else: 
            while not st.isempty() and st.peek() != '(' and getPriority (st.peek())>= getPriority (ch): 
                trgt+=st.pop() 
            st.push(ch) 
    while not st.isempty(): 
        trgt+=st.pop() 
    return trgt
source=input("Enter any Infix Expression: ") 
target=infix2postfix(source) 
print ("Required postfix Expression is:", target)