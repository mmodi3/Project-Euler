#
# Solution for Project Euler Problem 5 by Mitra Modi
#

import math

def pe5():
    answer = 1
    for i in range(1, 21):
        answer *= i // math.gcd(i, answer)
    return answer

if __name__ == "__main__":
    print(pe5())
