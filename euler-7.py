import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input().strip())

    primes = [2]
    for i in range(3, 10000000, 2):
        is_prime = True
        root = int(i**0.5)
        for p in primes:
            if p > root:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    for t_itr in range(t):
        n = int(input().strip())
        if n <= len(primes):
            print(primes[n-1])
        else:
            print("Prime number not found in the precomputed list.")