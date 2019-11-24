responses = {}

# Set a flag indicating whether the investigation continues.
polling_active = True

while polling_active:
    # Prompt inputting the respondent's name and answer.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the answer into the dictionary.
    responses[name] = response

    # See if anyone still wants to participate in the survey.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# End of investigation, display results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
