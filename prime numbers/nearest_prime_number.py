n = int(input())
def isprime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return True if count==0 else False
while True:
    n = n + 1
    if isprime(n):
        apn= n
        break
while True:
    n = n - 1
    if isprime(n):
        ppn = n
        break
ppd = n - ppn
apd = apn - n
if ppd < apd:
    print(ppn)
elif apd < ppd:
    print(apn)
else:
    print(ppn)
    print(apn)