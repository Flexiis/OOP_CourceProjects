#This is the first list
lst1=[7, -1, 3.1415, 9, 73, -12]
lst1.append("Hello World")
print(len(lst1))

#This is the second list and it is empty
lst2=[]
for i in range(40, 51, 1):
    lst2.append(i)
#Print each element in list1 1 time
for a in lst1:
    print(a)
#Clear List
lst1.clear()
#See If list is empty
for a in lst1:
    print(a)
    print("Clear Error")
#Step 14
print(lst2.pop())
print(lst2[2:6])
print(lst2[0:1])
#Step 15
lst2.insert(3, 8.1875)

print(lst1)
print(lst2)