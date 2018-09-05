#
# Solution for Project Euler Problem 4 by Mitra Modi
#
def palindromeproduct():
    i = 999
    j = 999
    res = 1
    while i > 99:
        while j > 99:
            if str(i*j) == str(i*j)[::-1] and i*j >= res:
                res = i * j
            j -= 1
        i -= 1
        j = i
    return res

if __name__ == "__main__":
    print(palindromeproduct())
