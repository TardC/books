filename = 'guest.txt'

username = input("Please enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(username)
