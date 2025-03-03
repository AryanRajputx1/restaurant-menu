menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 30,
    'Coffee': 80
}

print("Welcome to Python Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

while True:
    item = input("Enter the name of the item you want (or type 'exit' to stop): ").strip()

    if item.lower() == 'exit':
        break

    if item in menu:
        order_total += menu[item]
        print(f"{item} has been added to your order.")
    else:
        print(f"{item} is not in the menu.")

print(f"The total value of your order is Rs{order_total}.")
print("Thank you for visiting Python Restaurant!")
