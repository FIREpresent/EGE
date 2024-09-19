def isprime(num):
    for k in range(2,int(num**0.5)+1):
        if num % k == 0:
            return 0
    return 1

def func(x):
    while '00' not in x:
        x = x.replace('02', '101', 1)
        x = x.replace('11', '2', 1)
        x = x.replace('12', '21', 1)
        x = x.replace('010', '00', 1)
    return x

for i in range(70, 10000):
    x = '0' + '1'*i + '2'*i + '0'
    s = func(x)

    if isprime(sum(int(n) for n in s)):
        print(i)
        break
