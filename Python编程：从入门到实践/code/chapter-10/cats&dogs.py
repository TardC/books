def print_file(filename):
    """Read and print a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "The file " + filename + " does not exist!"
        # print(msg)
        pass
    else:
        print(contents)

print_file('cats.txt')
print_file('dogs.txt')
