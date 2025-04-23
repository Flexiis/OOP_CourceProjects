def sortList(lst1):
   # lst1 = [5.1, -3.4, 4.7, 0, 8.9]
    swaps = 1
    idx = 0
    while swaps != 0:
        print("swaps" , swaps)
        swaps = 0
        for idx in range(0, len(lst1[:-1])):
           if lst1[idx] > lst1[idx + 1]:
               swaps = swaps + 1
               lst1[idx], lst1[idx + 1] = lst1[idx + 1], lst1[idx]
               idx = idx + 1
               print(lst1, idx - 1, idx)
               print(swaps)


def main():
#    lst1.append(input("Enter list values "))
    f = open("dataIn.txt", "r")
    content_string = f.read()
    lst2 = content_string.split(",")
    lst1 = [float(ele) for ele in lst2]
    f.close()
    print(lst1)
    sortList(lst1)
    f = open("SortedDataOut.txt", "w")
    lst1STR = ','.join(map(str, lst1))
    f.write(lst1STR)


main()
