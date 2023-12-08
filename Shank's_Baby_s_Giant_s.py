# Shank's baby-giant-step alg
# for 3IS3 A4

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Towel 2017

from math import ceil, sqrt
import time


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None

start_time = time.time() 
print(bsgs(1234567890, 4950764383, 5915587277))
print("My program took", (time.time() - start_time)*1000.0, "to run")
#in milliseconds
