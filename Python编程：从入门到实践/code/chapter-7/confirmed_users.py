# First, create a list of unconfirmed users
# and a empty list to store confirmed users. 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Confirm every user, until there are not unconfirmed users,
# and move the confirmed user to the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
