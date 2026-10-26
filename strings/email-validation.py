def username(uname):
    if uname[0].isalpha():
        for j in range(1, len(uname)):
            if not uname[j].isalnum():
                if not uname[j] in {'.', '_'}:
                    return False
        else:
            return True
    else:
        return False

def domain(do):
    for j in range(len(do)):
        if not do[j].isalnum():
            return False
    return True

def extension(ex):
    for j in range(len(ex)):
        if not ex[j].isalpha():
            return False
    else:
        return True

e = input()

new_s = e.replace('.', '@')
s = new_s.split('@')

for i in range(len(s)):
    if i == 0:
        if not username(s[i]):
            print("Invalid")
            break
        next_char = len(s[i])
        if not e[next_char] == '@':
            print("Invalid")
            break
    elif i == 1:
        if not domain(s[i]):
            print('Invalid!')
            print("Domain1")
            break
        next_char = len(s[0]) + len(s[i]) + 1
        if not e[next_char] == '.':
            print("Invalid")
            break
    else:
        if not extension(s[i]):
            print("Invalid!")
            break
else:
    print('Valid!')