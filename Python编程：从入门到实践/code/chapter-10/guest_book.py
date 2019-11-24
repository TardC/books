filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        username = input("Please enter your name: ")
        print("Hello, " + username)
        file_object.write(username + " logined.\n")
