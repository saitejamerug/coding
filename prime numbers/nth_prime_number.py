n=int(input())
def isprime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return True if count==2 else False
count=0
num=2
while True:
    if isprime(num):
        count += 1
    if count==n:
        print(num)
        break
    num += 1