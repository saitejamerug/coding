def palindrome(s):
    le, ri = 0, len(s) - 1
    while le < ri:
        if s[le] != s[ri]:
            return False
        le += 1
        ri -= 1
    return True
def remove_one_char(s):
    le, ri = 0, len(s) -1
    if palindrome(s):
        return True
    while le < ri:
        if s[le] != s[ri]:
            les = s[le+1: ri+1]
            ris = s[le: ri]
            if palindrome(les) or palindrome(ris):
                return True
        le += 1
        ri -= 1
    return True
S = input()
res = remove_one_char(S)
print(res)