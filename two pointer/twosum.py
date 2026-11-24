def twosum(l, tar):
    s, e = 0, len(l) - 1
    while s < e:
        Sum = l[s] + l[e]
        if Sum == tar:
            return [s+1, e+1]
        elif Sum < tar:
            s += 1
        else:
            e -= 1
    return [-1, -1]
li = list(map(int, input().split()))
Tar = int(input())
print(twosum(li, Tar))