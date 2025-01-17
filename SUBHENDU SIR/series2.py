#1-3+5-7+9 find the sum upto n terms
n = int(input("Enter the number of terms: "))
i = 1
s = 0  
while i <= n:       #1<=5
    j = 1           
    while j <= i:   #1<=1
        if j % 2 != 0:  
            term = 2 * j - 1  #1
            if i % 2 != 0:  
                s += term #1 
            else:  
                s -= term #1-3
        j += 1  #2
    i += 1  
print("The sum of the series up to", n, "terms is:", s)