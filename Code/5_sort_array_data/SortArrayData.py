def sortList(lst1):
   # lst1 = [5.1, -3.4, 4.7, 0, 8.9]
    swaps = 1
    idx = 0
    while swaps != 0:
        print("swaps" , swaps)
        swaps = 0
        for idx in range(0, len(lst1[:-1])):
           if lst1[idx] < lst1[idx + 1]:
               swaps = swaps + 1
               lst1[idx], lst1[idx + 1] = lst1[idx + 1], lst1[idx]
               idx = idx + 1
               print(lst1, idx - 1, idx)


def main():
#    lst1.append(input("Enter list values "))
    lst1 = [5.1, -3.4, 4.7, 0, 8.9]
    sortList(lst1)


main()
