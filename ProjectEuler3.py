#
# Solution for Project Euler Problem 3 by Mitra Modi
#
from math import *

def isprime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if i % n == 0:
                return False
        return True

def gp():
    num = 600851475143
    for i in range(600851475143):
        while isprime(i) and num % i == 0:
            if num == i:
                return i
            num = num/i


if __name__ == "__main__":
    print(gp())
