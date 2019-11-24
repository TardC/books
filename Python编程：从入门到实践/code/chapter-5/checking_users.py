# All usernames stored in current_users are lower case. So checking
# lower case of new username is ok.


current_users = ['tom', 'eric', 'admin', 'lily', 'john']

new_users = ['david', 'yuki', 'helene', 'lily', 'John']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Username is used. Please try others.")
    else:
        print("Usernama is available.")
