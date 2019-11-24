vacation_spots = []
prompt = "If you could visit one place in the world,"
prompt += " where would you go?"
prompt += "\n(Enter 'quit' to end the program.) "

active = True
while active:
    spot = input(prompt)
    if spot == 'quit':
        active = False
    else:
        vacation_spots.append(spot)

print(vacation_spots)
