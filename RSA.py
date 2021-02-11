#runtime 3.5 python 
import math 
import random 

def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True 

def get_prime(size):
    while True:
        p = random.randrange(size, 2 * size)
        if is_prime(p):
            return p

def lcm(a, b):
    return a*b//math.gcd(a, b)

def get_e(lambda_n):
    for e in range(10, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
        return False
    
def get_d(e, lambda_n):
    for d in range(10, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

def factor(n):
    for p in range(10, n):
        if n % p == 0:
            return p, n//p

#key generation done by Alice (secert)
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated primes", p , q)

#compute n = p*q
n  = p*q
print("Modolus n:", n)

#Compute lambda(n) (lcm(n) = λ(n) = lcm(λ(p),λ(q), λ(q) = q − 1,lcm(a,b) = |ab|/qcd(a,b))
lambda_n = lcm(p-1, q-1)
print("Lambda n", lambda_n)

#integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime
e = get_e(lambda_n)
print("Public exponent:", e)

#Determine d as d ≡ e−1 (mod λ(n))
d = get_d(e, lambda_n)
print("Secret exponent:", d)

# Done with key generation:
print("Public key (e,n:", e, n)
print("Secert key[d]", d)
