def rev_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    le, ri = 0, len(s) - 1
    s = list(s)
    while le < ri:
        if s[le] not in vowels:
            le += 1
        elif s[ri] not in vowels:
            ri -= 1
        else:
            s[le], s[ri] = s[ri], s[le]
            le += 1
            ri -= 1
    s = "".join(s)
    return s
S = input()
res = rev_vowels(S)
print(res)