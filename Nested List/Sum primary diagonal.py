# Sum of Primary Diagonal
nl = []
rows = int(input())
columns = int(input())
for i in range(rows):
    l = []
    for j in range(columns):
        l.append(int(input()))
    nl.append(l)

Sum = 0
for i in range(rows):
    for j in range(columns):
        if i == j:
            Sum += nl[i][j]
print("Primary Diagonal Sum:", Sum)