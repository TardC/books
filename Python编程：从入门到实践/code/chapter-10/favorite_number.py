import json

def get_favorite_number():
    """Get your favorite number from the file, if it exists."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def input_favorite_number():
    """Input your favorite number and store it."""
    filename = 'favorite_number.json'
    favorite_number = input("Enter your favorite number: ")
    favorite_number = int(favorite_number)
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
    return favorite_number

def show_favorite_number():
    favorite_number = get_favorite_number()
    if favorite_number is not None:
        print("I know your favorite number! It's " +
            str(favorite_number) + ".")
    else:
        favorite_number = input_favorite_number()
        print("Your favorite number is " + str(favorite_number) + ".")

show_favorite_number()
