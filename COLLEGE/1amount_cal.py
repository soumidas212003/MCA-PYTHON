#write a python program to calculate the bill amount for an item given its quantity sold, value, discount and tax
qty=float(input("Enter the quantity of item sold: "))       #5
val=float(input("Enter the value of the item: "))           #100
discount=float(input("Enter the discount percentage: "))    #10
tax=float(input("Enter the tax: "))                         #5
amt=qty*val     #5*100=500
discount=(amt*discount)/100 #(500*10)/100=50
total=amt-discount #500-50=450
tax_amt=(total*tax)/100 #(450*5)/100=22.5
total=total+tax_amt #450+22.5=472.5
print("----Bill----")
print("Quantity sold:\t",qty)
print("Price per item:\t",val)
print("Total amount:\t",total)