def palindrome(s):
    le, ri = 0, len(s) - 1
    while le < ri:
        if s[le] != s[ri]:
            return False
        le += 1
        ri -= 1
    return True
S = input()
res = palindrome(S)
print(res)