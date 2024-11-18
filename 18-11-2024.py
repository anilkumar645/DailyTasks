""" Encapuslation

While modeling real-life objects with object oriented programming, we ensure to bundle related information together to 
clearly separate information of different objects.

Bundling of related properties and actions together is called Encapsulation.

Classes can be used to bundle related properties and actions. """






class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_call(self,number):
        print("calling..{}".format(number))

mobile_obj = Mobile("iPhone 12 Pro", "12 MP")
mobile_obj.make_call(9876543210)



""" BANK """

 
#Example:

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Private attributes
        self.__account_holder = account_holder
        self.__balance = balance
 
    # Getter for account holder
    def get_account_holder(self):
        return self.__account_holder
 
    # Setter for account holder (if name needs to be updated)
    def set_account_holder(self, new_name):
        if new_name.strip():  # Ensure the name is not empty
            self.__account_holder = new_name
        else:
            print("Invalid account holder name!")
 
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")
 
    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")
 
    # Getter for balance (no setter to prevent direct modification)
    def get_balance(self):
        return self.__balance
 
 
# Usage example
account = BankAccount("John Doe", 1000)
print("Account Holder:", account.get_account_holder())
print("Initial Balance:", account.get_balance())
 
# Deposit and withdraw
account.deposit(500)
account.withdraw(300)
 
# Try updating the account holder
account.set_account_holder("Jane Doe")
print("Updated Account Holder:", account.get_account_holder())
 



# Online shopping

class ShoppingCart:
    def __init__(self):
        # Private attributes
        self.__items = {}
        self.__total_price = 0.0
 
    # Method to add an item to the cart
    def add_item(self, item_name, price, quantity=1):
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.")
            return
 
        if item_name in self.__items:
            self.__items[item_name]["quantity"] += quantity
        else:
            self.__items[item_name] = {"price": price, "quantity": quantity}
 
        self.__update_total()
        print(f"Added {quantity} x {item_name} to the cart.")
 
    # Method to remove an item from the cart
    def remove_item(self, item_name):
        if item_name in self.__items:
            del self.__items[item_name]
            self.__update_total()
            print(f"Removed {item_name} from the cart.")
        else:
            print(f"{item_name} is not in the cart.")
 
    # Method to get the current cart items
    def get_items(self):
        return self.__items.copy()
 
    # Method to get the total price of items in the cart
    def get_total_price(self):
        return self.__total_price
 
    # Private method to update the total price
    def __update_total(self):
        self.__total_price = sum(
            item["price"] * item["quantity"] for item in self.__items.values()
        )
 
    # Method to display the cart
    def display_cart(self):
        if not self.__items:
            print("Your shopping cart is empty.")
        else:
            print("\nShopping Cart:")
            for item, details in self.__items.items():
                print(f"- {item}: ${details['price']} x {details['quantity']}")
            print(f"Total Price: ${self.__total_price:.2f}")
 
 
# Usage Example
cart = ShoppingCart()
cart.add_item("Laptop", 1200.50, 1)
cart.add_item("Headphones", 150.99, 2)
cart.display_cart()
 
cart.remove_item("Laptop")
cart.display_cart()
 
print("Cart Items:", cart.get_items())
print("Total Price:", cart.get_total_price())