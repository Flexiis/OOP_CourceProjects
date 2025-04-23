numb = input("Number of students in group: ")
numb2 = int(numb)
lst1 = []
lstTXT = ""
for i in range(0, numb2, 1):
    name1 = input("Name of students in group: ")
    lst1.append(name1)
print(lst1)
print(len(lst1))

#Open
f = open("Test1.txt", "w")
lst1STR = ' '.join(map(str, lst1))
f.write(lst1STR)


lst1.clear()
print(lst1)
print(len(lst1))
f.close()

f = open("Test1.txt", "r")
content_string = f.read()
content_list = content_string.split(" ")
f.close()
print(content_list)
for element in content_list:
    print(len(element))