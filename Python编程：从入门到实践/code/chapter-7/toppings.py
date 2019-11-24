prompt = "\nPlease input a pizza topping:"
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print("We will add " + topping + " on your pizza.")


active = True
while active:
    topping = input(prompt)
    
    if topping == 'quit':
        active = False
    else:
        print("We will add " + topping + " on your pizza.")
