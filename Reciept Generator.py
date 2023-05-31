store_name = input("Enter the name of the store: \n")

item_prices = []
items_name = []
total_items = int(input("Enter the number of total items purchased: \n"))
for item in range(1, total_items + 1):
    price = int(input("Enter the price of the item :"))
    name = input("Enter the name of the item :")
    items_name.append(name)
    item_prices.append(price)
print("-" * 50)
print(f"           {store_name}             ")
print("-" * 50)
for i in range(total_items):
    print(f"{items_name[i]}: {'-' * 40} {item_prices[i]:.2f}")
print("-" * 50)
print(f"Total : {sum(item_prices):.2f}")
print("-" * 50)
