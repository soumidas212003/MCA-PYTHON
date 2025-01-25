'''
records=[["chi",20.0],["beta",50.0],["alpha",50.0]]
The ordered list of scores is [20.0,50.0], so the second lowest score is 50.0. There are two students with that score: ["beta","alpha"]. Ordered alphabetically, the names are printed as:

alpha
beta

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
'''

n = int(input())  # Number of students
records = []  # List to store (name, grade) tuples
grades = []   # List to store all grades

for i in range(n):
    nm = input()  # Read student's name
    grd = float(input())  # Read student's grade
    records.append((nm, grd))  # Append tuple to records
    grades.append(grd)  # Append grade to grades list

# Find unique grades and sort them
uniq_grades = sorted(set(grades))

# The second lowest grade
sec_lowest = uniq_grades[1]

# Collect names with the second lowest grade
sec_lowest_names = [nm for nm, grd in records if grd == sec_lowest]

# Sort the names alphabetically
sec_lowest_names.sort()

# Print the sorted names
for nm in sec_lowest_names:
    print(nm)
