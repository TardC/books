def make_great(magicians):
    """Add 'the Great' to the name of all magicians."""
    index = 0
    while index < len(magicians):
        magicians[index] = 'the Great ' + magicians[index]
        index += 1
    return magicians

def show_magicians(magicians):
    """Show the name of all magicians in list magicians."""
    for magician in magicians:
        print(magician)

magicians = ['Abc', 'Qwer', 'He']
modified_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(modified_magicians)
