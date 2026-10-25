nl=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(nl)):
    for j in range(len(nl[0])):
        if i != 0:              # top ele
            print(nl[i-1][j])
        if j != 0:   # left ele
            print(nl[i][j-1])
        if j != len(nl)-1:   # right ele
            print(nl[i][j+1])
        if i != len(nl)-1:      # bottom ele
            print(nl[i+1][j])
    print()