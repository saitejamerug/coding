nl=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(nl)):
    for j in range(len(nl[0])):
        if i != 0 and j != 0:   # top left
            print(nl[i-1][j-1])
        if i != 0 and j != len(nl[0]) - 1:  # top right
            print(nl[i-1][j+1])
        if i != len(nl) - 1 and j != 0:
            print(nl[i+1][j-1])
        if i != len(nl)-1 and j != len(nl[0])-1:
            print(nl[i+1][j+1])
    print()
