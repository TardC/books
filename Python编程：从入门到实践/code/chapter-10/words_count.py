def count_words(filename):
    """Calculate how many words a file approximately contains."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
       # msg = "Sorry, the file " + filename + " does not exist."
       # print(msg)
       pass
    else:
        # Calculate how many words this file approximately contains.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
