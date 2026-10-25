def prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return True if count == 2 else False

nl=[[1, 2, 3], [4, 5, 6, 10], [7, 8, 9], [11, 12, 13, 14, 15]]

for i in range(len(nl)):
    for j in range(len(nl[0])):
        if prime(nl[i][j]):
            print(nl[i][j])
    print()