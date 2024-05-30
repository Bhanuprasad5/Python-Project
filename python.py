class MenuItem: # parent class
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FoodItem(MenuItem): # derived/child class
    def __init__(self, name, price):
        super().__init__(name, price)

class BeverageItem(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

class Restaurant:
    def __init__(self):
        self.menu = {
            'foods': [
                FoodItem("Biryani - chicken", 200),
                FoodItem("Biryani - mutton", 250),
                FoodItem("Biryani - Prawns", 300),
                FoodItem("Tandoori - roti - chicken", 250),
                FoodItem("Tandoori - roti - mutton", 300),
                FoodItem("Kadai chicken", 300),
                FoodItem("Boti curry with chapati", 250),
                FoodItem("Egg fried rice with prawns", 150),
                FoodItem("Veg fried rice with pasta and paneer", 150),
                FoodItem("Sire paay with Roti", 300),
                FoodItem("Mutton pulav with nalli nahaari", 500)
            ],
            'sweets': [
                MenuItem("Kaddu ki kheer", 110),
                MenuItem("Kashmiri kheer", 150),
                MenuItem("Mango rabdi", 150),
                MenuItem("Leechee malai", 200),
                MenuItem("Qubani ka meetha", 200),
                MenuItem("Dry and wet fruits icecream malai", 300)
            ],
            'beverages': [
                BeverageItem("Fanta", 60),
                BeverageItem("Goli soda", 20),
                BeverageItem("Limka", 30)
            ]
        }
        self.order = []
        self.total_bill = 0

    def display_menu(self, category):
        print(f"\n{category.capitalize()} Items:")
        for i, item in enumerate(self.menu[category], start=1):
            print(f"{i}. {item.name} - ${item.price}")

    def add_to_order(self, item, quantity):
        self.order.append((item, quantity))
        self.total_bill += item.price * quantity

    def display_order(self):
        print("\n" + "-"*50)
        print(" " * 18 + "ORDER")
        print("-"*50)
        print("{:<30} {:<10} {:<10}".format("Item", "Quantity", "Price ($)"))
        for item, quantity in self.order:
            print("{:<30} {:<10} {:<10}".format(item.name, quantity, item.price * quantity))
        print("-"*50)
        print("{:<40} {:<10}".format("Total Bill", f"${self.total_bill}"))
        if self.total_bill > 1500:
            print("Take-away Parcel: Leechee Malai Sweet (Discount)")

def main():


    restaurant = Restaurant()
    while True:
        print("\nOptions:")
        print("1. Food Items")
        print("2. Sweets and Deserts")
        print("3. Cool Drinks and Beverages")
        print("4. Display Current Order")
        print("5. Add Tip")
        print("6. Thank you, Visit Again")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                restaurant.display_menu('foods')
                selection = input("Enter the number of the food item you'd like to order (or 'b' to go back): ")
                if selection == 'b':
                    break
                elif selection.isdigit() and 0 < int(selection) <= len(restaurant.menu['foods']):
                    selected_item = restaurant.menu['foods'][int(selection) - 1]
                    quantity = int(input("Enter the quantity: "))
                    restaurant.add_to_order(selected_item, quantity)
                else:
                    print("Invalid selection. Please try again.")
        elif choice == '2':
            while True:
                restaurant.display_menu('sweets')
                selection = input("Enter the number of the sweet item you'd like to order (or 'b' to go back): ")
                if selection == 'b':
                    break
                elif selection.isdigit() and 0 < int(selection) <= len(restaurant.menu['sweets']):
                    selected_item = restaurant.menu['sweets'][int(selection) - 1]
                    quantity = int(input("Enter the quantity: "))
                    restaurant.add_to_order(selected_item, quantity)
                else:
                    print("Invalid selection. Please try again.")
        elif choice == '3':
            while True:
                restaurant.display_menu('beverages')
                selection = input("Enter the number of the beverage item you'd like to order (or 'b' to go back): ")
                if selection == 'b':
                    break
                elif selection.isdigit() and 0 < int(selection) <= len(restaurant.menu['beverages']):
                    selected_item = restaurant.menu['beverages'][int(selection) - 1]
                    quantity = int(input("Enter the quantity: "))
                    restaurant.add_to_order(selected_item, quantity)
                else:
                    print("Invalid selection. Please try again.")
        elif choice == '4':
            restaurant.display_order()
        elif choice == '5':
            try:
                tip = float(input("Enter tip amount: "))
                restaurant.total_bill += tip
                print("Tip added successfully.")
            except ValueError:
                print("Invalid tip amount. Please enter a valid number.")
        elif choice == '6':
            restaurant.display_order()
            print("💐Thank you! Visit again.💐")
            break
        else:
            print("Invalid choice. Please select again.")

main()

print("\n")
print("\t\t\t\t\t\t\t\t **********K-M Restaurant********** \t\t\t\t\t\t\t\t")
print("\t\t\t\t\t\t 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
print("\t\t\t\t\t\t\t\t 5-2-37\19A/1, Fathepura Street, NAVABHARAT \t\t\t\t\t\t\t")
print("\t\t\t\t\t\t\t\t Opposite TowerCircle, Church road \t\t\t\t\t\t")
print("\t\t\t\t\t\t\t\t Palwancha, Karimnagar-Kothagudem, TS - 505001 \t\t\t\t\t")
print("\t\t\t\t\t\t\t\t\t\t 🌸🌸🌸")
