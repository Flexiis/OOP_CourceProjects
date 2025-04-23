import sys
from sys import argv
import math
dis = float()
valid = bool()


#Fill in the agruments in the command terminal using spaces as the argument splitter when runnig the program


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

def getresults(a, b, c):
    # Discriminant
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
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

def main(argc, argv):
    i = 0
    for arg in argv:
        print("argument[%d] is %s" % (i, arg))
        i = i + 1
    a = float()
    b = float()
    c = float()
    if argc == 4:
        a = float(argv[1])
        b = float(argv[2])
        c = float(argv[3])
    else:
        print("Error")

    X = getresults(a, b, c)
    if X[0] == True:
        print("Valid solution")
        print(X[1])
    else:
        print("Not a valid solution")

if __name__ == '__main__':
    main(len(argv), argv)