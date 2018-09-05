#
# Solution for Project Euler Problem 2 by Mitra Modi
#
def FibEvenSum():
    l = 1
    m = 2
    sum = 0
    while l <= 4000000:
        n = l
        l = m
        m = n + l
        if l % 2 == 0:
            sum += l
    return sum

if __name__ == "__main__":
    print(FibEvenSum())
