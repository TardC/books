def read_file(filename):
    """Read and return a file's contents."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "The file " + filename + " does not exist!"
        print(msg)
    else:
        return contents

filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    contents = read_file(filename)
    try:
        counts = contents.lower().count('the')
    except AttributeError:
        pass
    else:
        msg = "There are " + str(counts) + " 'the' in the file " + filename + "."
        print(msg)
