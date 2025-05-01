import string
class stack:
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
def postfixevaluation(src):
    st=stack()
    for ch in src:
        if ch.isdigit():
            st.push(int(ch))
        else:
            var1=st.pop()
            var2=st.pop()
            match ch:
                case '+':
                    var3=var2+var1
                case '-':
                    var3=var2-var1
                case '*':
                    var3=var2*var1
                case '/':
                    var3=var2/var1
            st.push(var3)
    return (st.pop())
source=input("Enter any postfix expression: ")
result=postfixevaluation(source)
print("Required postfix expression is: ",result)
                