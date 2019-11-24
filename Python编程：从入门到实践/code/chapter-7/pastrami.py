sandwich_orders = ['tuna', 'pastrami', 'cheese',
                  'pastrami', 'apple', 'pastrami']

print("Pastrami have been sell out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
