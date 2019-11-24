import json

def get_stored_username():
    """If the username has been stored, then get it."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt the user to enter his username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user, and point out his name."""
    username = get_stored_username()
    if username:
        answer = input("Are you " + username + "? (yes/no) ")
        if answer.lower() == 'yes':
            print("Welcome back, " + username + "!")
        elif answer.lower() == 'no':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
        else:
            print("Please enter accoding to the prompt.")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
