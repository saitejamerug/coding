def binary_search(l, k):
    l.sort()
    s, e = 0, len(l) - 1
    while s < e:
        mid = (s + e) // 2
        if l[mid] == k:
            return "Found"
        elif l[mid] < k:
            s = mid + 1
        else:
            e = mid - 1
    return "Not Found"
l = list(map(int, input().split()))
target = int(input())
result = binary_search(l, target)
print(result)