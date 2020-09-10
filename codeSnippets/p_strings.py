my_result = 40 /10
print(my_result)

def my_func(a,b):
    return a - b

print(my_func(10,20))

def my_converter(word):
    return word.capitalize()

print(my_converter("hans"))

def my_converter2(word, o_letter, n_letter):
    return word.replace(o_letter, n_letter)

print(my_converter2("hans","h","H"))

myList = [1,2,3,4,5]

average = sum(myList)/len(myList)

print(average)