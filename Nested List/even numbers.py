def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

nl=[[1, 2, 3], [4, 5, 6, 10], [7, 8, 9], [11, 12, 13, 14, 15]]

for i in range(len(nl)):
    for j in range(len(nl[i])):
        if even(nl[i][j]):
            print(nl[i][j])
    print()