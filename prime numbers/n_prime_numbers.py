n=int(input())
def isprime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return True if count == 2 else False

i = 2
count = 0
comma = 1
while True:
    if isprime(i):
        count += 1
        if count > comma:
            print(",", end=" ")
        print(i, end="")
    if count == n:
        break
    i += 1