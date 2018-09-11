#
# Solution for Project Euler Problem 6 by Mitra Modi
#

def pe6():
    squareofsums = 0
    sumofsquares = 0
    for i in range(1, 101):
        sumofsquares += i**2
        squareofsums += i
    squareofsums *= squareofsums
    return  squareofsums - sumofsquares

if __name__ == "__main__":
    print(pe6())
