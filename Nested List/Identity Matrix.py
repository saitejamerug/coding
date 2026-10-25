# Identity Matrix
r = int(input("No.of rows:"))
c = int(input("No.of columns:"))
if r == c:
    count = 0
    # Creation of Nested list
    nl = list()
    for i in range(r):
        l = []
        for j in range(c):
            l.append(int(input()))
        nl.append(l)

    # To inspect Identity matrix or not
    for i in range(len(nl)):
        for j in range(len(nl)):
            if i == j and nl[i][j] == 1:
                count += 1
            elif i != j and nl[i][j] == 0:
                count += 1
            else:
                print("Not an Identity Matrix")
                break
    if count == r * r:
        print("It's an Identity Matrix")
else:
    print("Rows & columns must be same")