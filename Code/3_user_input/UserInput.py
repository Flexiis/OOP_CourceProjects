Name = input("Enter a name: ")
HeightBegin = input("Input a height: ")
Height = int(HeightBegin)

if Height > 180:
    print(Name + " is taller than the limit")
else:
    print(Name + " is not taller than the limit")