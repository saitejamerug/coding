nl = []
rows = int(input())
columns = int(input())
for i in range(rows):
    l = []
    for j in range(columns):
        l.append(int(input()))
    nl.append(l)

for i in range(rows):
    Sum = 0
    for j in range(columns):
        Sum += nl[i][j]
    print(f"{i+1} inner list sum:", Sum)