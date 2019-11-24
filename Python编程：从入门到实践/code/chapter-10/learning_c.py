filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'C')
    print(contents)
