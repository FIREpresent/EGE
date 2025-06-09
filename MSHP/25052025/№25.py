import math


def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            sieve[i * i: limit + 1: i] = [False] * len(sieve[i * i: limit + 1: i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes


primes = sieve(16007)

results = []

start = 256123000
end = 256234000

for N in range(start, end + 1):
    if N % 2 == 0:
        p = 2
    else:
        max_prime = int(math.isqrt(N))
        p = None
        for prime in primes:
            if prime > max_prime:
                break
            if N % prime == 0:
                p = prime
                break
        if p is None:
            continue  # N is prime, M=0

    temp = N
    k = 0
    while temp % p == 0:
        temp //= p
        k += 1
    m = temp  # m = N // (p^k)

    if m == 1:
        if k >= 3:
            M = (p ** (k - 1)) + (p ** (k - 2))
        else:
            continue
    else:
        if m % 2 == 0:
            q = 2
        else:
            max_q_prime = math.isqrt(m)
            q = None
            for prime in primes:
                if prime > max_q_prime:
                    break
                if m % prime == 0:
                    q = prime
                    break
            if q is None:
                q = m
        M = (N // p) + (N // q)

    if M % 10000 == 1234:
        results.append((N, M))

results.sort(key=lambda x: -x[1])

for n, m in results:
    print(n, m)