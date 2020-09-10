mydict1 = {"apple":2,"banana":3,"kiwi":2, "melon":10}

mydict2 = {"apple":"green","banana":"yellow","kiwi":"braun", "melon":"light yellow"}
#print(mydict2)


#mydict3 = {"apple":"green","banana":"yellow","kiwi":"braun", "melon":"light yellow", "melon":"light yellow", "melon":"pink"}
#print(mydict3)

#accessing items
# input key --> output value
#print(mydict1["apple"])

#print(mydict1.keys())
#print(mydict1.values())

print(type(mydict1))
#dict keys and values to list

list_of_dict_values = list(mydict1.values())
list_of_dict_keys = list(mydict1.keys())
print(list_of_dict_values)
print(list_of_dict_keys)
print(type(list_of_dict_values))
print(type(list_of_dict_keys))
"""
#dicts + lists
mydict5 = {"apple":[2,22],"banana":[3,33],"kiwi":[2,22], "melon":[10,1010]}
print(mydict5)

#methods deleting
mydict5.popitem()
print(mydict5)
mydict5.pop("banana")
del mydict5["kiwi"]
print(mydict5)
#methods adding key value pair
mydict5.update({"grapefruit":3})
print(mydict5)

print("-----")
#iterating over/traversing through a dict
#shows you keys

for fruits in mydict2:
    print(fruits)

#shows you the values
for fruits in mydict2.values():
    print(fruits)

#shows you tuples of key value pairs
for fruits in mydict2.items():
    print(fruits)
"""

for fruits in mydict2.keys():
    print(fruits + " tasty")
