# substring in main string
s = input()
t = input()
for i in range(len(s) - len(t) + 1):
    sb = []
    for j in range(i, i + len(t)):
        sb.append(s[j])
    sb = ''.join(sb)
    if sb == t:
        print("Found")
        break
else:
    print("Not Found")