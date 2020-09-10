myList = [1,2,3,4,5]
print(myList)
print("---------")
#accessing items
print(myList[0])
print(myList[2])
print(myList[-1])
print(myList[-2])
print("---------")
print(myList[0:2])
print(myList[:2])
print(myList[1:5]) # 5 element is excluded
print(myList[1:])

print("---------")
#modifying items
myList[0] = 10
myList[1] = 20
myList[2] =  "Max"
myList[3:] = ["Lisa","Torsten"]
print(myList)

print("---------")
#apply functions
myList.append(11)
print(myList)
print(len(myList))
myList.remove(11)
print(myList)
print(len(myList))

myList.append(33)
myList.append(33)
print(myList)
print(myList.count(33))

print("---------")
#iterating over/traversing through a list
myList2 = [10,20,30,40,50]
myList3 = ["Maria","Max","Martin","Maja","Mona"]
myList4 = []

for items in myList2:
    print(items)

for items in myList2:
    print(items + 1)

for names in myList3:
    print(names)

for names in myList3:
    print(names.upper())

for items in myList4:
    print(items)

print("-------")
print(max(5,2,3))