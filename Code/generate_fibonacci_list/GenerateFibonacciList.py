def getFibonacciList(lmt):
    lst1 = [0, 1]
    x = 2
    while lst1[-1] <= int(lmt):
        lst1.append(lst1[x-1] + lst1[x-2])
        x += 1
    if lst1[-1] > lmt:
        del lst1[-1]
    return lst1

def main():
    lmt = int(input("Max Limit: "))
    print(getFibonacciList(lmt))

main()