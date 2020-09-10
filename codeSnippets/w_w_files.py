filename="resources/text_example_1.txt"
file= open(filename, mode='r') # 'w' for write mode
text = file.read()
print(text)
file.close()


