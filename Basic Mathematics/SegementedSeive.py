def isPrime(n):
    if n <= 1:
        return []
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    primes = []
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)
    return primes

def Segmented_seive(l, r):
    primes = isPrime(int(r**0.5) + 1)  # Generate primes up to sqrt(r)
    dummy = [True] * (r - l + 1)
    for p in primes:
        low = max(p * p, ((l + p - 1) // p) * p)  # Find the first multiple of p in the range [l, r]
        for i in range(low, r + 1, p):
            dummy[i - l] = False
    for i in range(l, r + 1):
        if dummy[i - l]:
            print(i)

Segmented_seive(30, 64)
