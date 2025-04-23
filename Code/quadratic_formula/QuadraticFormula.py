import math
a = float(input("aX^2 "))
b = float(input("bX "))
c = float(input("c "))
dis = float()
valid = bool()

def getresults(a, b, c):
    # Discriminant
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    #choose what to do when the discriminant is which value
    if dis > 0:
        x1 = (-b + sqrt_val) / (2 * a)
        x2 = (-b - sqrt_val) / (2 * a)
        awn = [x1, x2]
        valid = True
    elif dis == 0:
        x1 = (-b / (2 * a))
        awn = [x1]
        valid = True
    else:
        awn = []
        valid = False

    return valid, awn

def main(a, b, c):
    X = getresults(a, b, c)
    #if validation is true print x
    if X[0] == True:
        print("Valid solution")
        print(X[1])
    #discriminant negative, print not a valid solution
    else:
        print("Not a valid solution")

main(a, b, c)