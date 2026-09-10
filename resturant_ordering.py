import csv
from datetime import datetime


# =========================================================
# FOOD ITEM
# =========================================================

class FoodItem:

    def __init__(self, food_id, name, category, price, portions=None):
        self.food_id = food_id
        self.name = name
        self.category = category
        self.price = price
        self.portions = portions

    def display(self):
        if self.portions:
            prices = " | ".join(
                f"{p}: ₹{price}" for p, price in self.portions.items()
            )
            print(f"{self.food_id:<4} {self.name:<28} {self.category:<12} {prices}")
        else:
            print(f"{self.food_id:<4} {self.name:<28} {self.category:<12} ₹{self.price}")


# =========================================================
# ORDER
# =========================================================

class Order:

    def __init__(self, customer, token, order_type):
        self.customer = customer
        self.token = token
        self.order_type = order_type
        self.items = {}
        self.table = ""
        self.phone = ""
        self.address = ""

    def add_item(self, food, quantity, portion=None):

        key = f"{food.food_id}-{portion}"

        if key in self.items:
            self.items[key]["quantity"] += quantity
        else:
            price = food.price

            if portion:
                price = food.portions[portion]

            self.items[key] = {
                "food": food,
                "quantity": quantity,
                "portion": portion,
                "price": price
            }

    def remove_item(self, key, quantity):

        if key not in self.items:
            return False

        if quantity >= self.items[key]["quantity"]:
            del self.items[key]
        else:
            self.items[key]["quantity"] -= quantity

        return True

    def subtotal(self):

        total = 0

        for item in self.items.values():
            total += item["price"] * item["quantity"]

        return total

    def quantity(self):

        return sum(item["quantity"] for item in self.items.values())

    def waiting_time(self):

        if self.quantity() <= 2:
            return 15
        elif self.quantity() <= 4:
            return 25
        else:
            return 35

    def show_cart(self):

        if not self.items:
            print("\nCart is empty.")
            return

        print("\n" + "=" * 65)
        print("YOUR CART")
        print("=" * 65)

        for item in self.items.values():

            food = item["food"]
            portion = f" ({item['portion']})" if item["portion"] else ""

            amount = item["price"] * item["quantity"]

            print(
                f"{food.name}{portion} - "
                f"{item['quantity']} x ₹{item['price']} = ₹{amount}"
            )

        print("-" * 65)
        print(f"Subtotal: ₹{self.subtotal():.2f}")


# =========================================================
# RESTAURANT
# =========================================================

class Restaurant:

    def __init__(self):

        self.name = "SWADH"
        self.menu = []
        self.orders = []
        self.next_token = 1001

        # Tuple
        self.categories = (
            "Lunch",
            "Chinese",
            "Mandhi",
            "Drinks",
            "Desserts"
        )

        self.load_menu()

        # Set
        self.unique_categories = {
            food.category for food in self.menu
        }

    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    def load_menu(self):

        self.menu = [

            # Lunch
            FoodItem(101, "Chicken Biriyani", "Lunch", 180,
                     {"Half": 120, "Full": 180}),
            FoodItem(102, "Mutton Biriyani", "Lunch", 240,
                     {"Half": 160, "Full": 240}),
            FoodItem(103, "Egg Biriyani", "Lunch", 150,
                     {"Half": 100, "Full": 150}),
            FoodItem(104, "Veg Biriyani", "Lunch", 140,
                     {"Half": 90, "Full": 140}),
            FoodItem(105, "Normal Meals", "Lunch", 100),
            FoodItem(106, "Sadya Meals", "Lunch", 180),
            FoodItem(107, "Pazham Kanji", "Lunch", 100),
            FoodItem(108, "Chatti Choru", "Lunch", 140),

            # Chinese
            FoodItem(201, "Chicken Fried Rice", "Chinese", 170),
            FoodItem(202, "Egg Fried Rice", "Chinese", 150),
            FoodItem(203, "Veg Fried Rice", "Chinese", 130),
            FoodItem(204, "Chicken Noodles", "Chinese", 170),
            FoodItem(205, "Egg Noodles", "Chinese", 150),
            FoodItem(206, "Veg Noodles", "Chinese", 130),
            FoodItem(207, "Chicken Soup", "Chinese", 100),
            FoodItem(208, "Hot & Sour Soup", "Chinese", 90),

            # Mandhi
            FoodItem(301, "Peri Peri Chicken Mandhi", "Mandhi", 400,
                     {"Half": 220, "Full": 400}),
            FoodItem(302, "Alfaham Mandhi", "Mandhi", 420,
                     {"Half": 230, "Full": 420}),
            FoodItem(303, "Mutton Mandhi", "Mandhi", 500,
                     {"Half": 280, "Full": 500}),
            FoodItem(304, "Spicy Chicken Mandhi", "Mandhi", 400,
                     {"Half": 220, "Full": 400}),
            FoodItem(305, "Normal Chicken Mandhi", "Mandhi", 370,
                     {"Half": 200, "Full": 370}),

            # Drinks
            FoodItem(401, "Lemonade", "Drinks", 50),
            FoodItem(402, "Pepsi", "Drinks", 40),
            FoodItem(403, "Mint Lime", "Drinks", 60),
            FoodItem(404, "Fresh Lime", "Drinks", 50),
            FoodItem(405, "Orange Juice", "Drinks", 80),
            FoodItem(406, "Mango Juice", "Drinks", 90),
            FoodItem(407, "Pineapple Juice", "Drinks", 80),
            FoodItem(408, "Watermelon Juice", "Drinks", 80),
            FoodItem(409, "Grape Juice", "Drinks", 80),

            # Desserts
            FoodItem(501, "Vanilla Ice Cream", "Desserts", 70),
            FoodItem(502, "Chocolate Ice Cream", "Desserts", 80),
            FoodItem(503, "Strawberry Ice Cream", "Desserts", 80),
            FoodItem(504, "Butterscotch Ice Cream", "Desserts", 80),
            FoodItem(505, "Pista Ice Cream", "Desserts", 90),
            FoodItem(506, "Black Currant Ice Cream", "Desserts", 90),
            FoodItem(507, "Brownie with Ice Cream", "Desserts", 160)
        ]

    def show_menu(self):

        print("\n" + "=" * 80)
        print("                         SWADH MENU")
        print("=" * 80)

        print(f"{'ID':<4} {'Food':<28} {'Category':<12} Price")
        print("-" * 80)

        for food in self.menu:
            food.display()

        print("=" * 80)

    def find_food(self, food_id):

        for food in self.menu:
            if food.food_id == food_id:
                return food

        return None

    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------

    def search(self):

        word = input("\nSearch food/category: ").lower()

        found = [
            food for food in self.menu
            if word in food.name.lower()
            or word in food.category.lower()
        ]

        if not found:
            print("No food found.")
            return

        print("\nSearch Results")
        print("-" * 70)

        for food in found:
            food.display()

    # -----------------------------------------------------
    # CREATE ORDER
    # -----------------------------------------------------

    def create_order(self):

        customer = input("\nCustomer name: ").strip()

        if not customer:
            print("Name cannot be empty.")
            return None

        print("\nOrder Type")
        print("1. Dine-in")
        print("2. Takeaway")
        print("3. Online Delivery")

        while True:

            choice = input("Choose: ")

            if choice == "1":
                order_type = "Dine-in"
                break
            elif choice == "2":
                order_type = "Takeaway"
                break
            elif choice == "3":
                order_type = "Online Delivery"
                break
            else:
                print("Invalid choice.")

        order = Order(
            customer,
            self.next_token,
            order_type
        )

        self.next_token += 1

        if order_type == "Dine-in":

            order.table = input("Table number: ")

        elif order_type == "Online Delivery":

            order.phone = input("Phone number: ")
            order.address = input("Delivery address: ")

        self.orders.append(order)

        print(
            f"\nOrder created successfully!"
            f"\nToken Number: {order.token}"
        )

        return order

    # -----------------------------------------------------
    # ADD FOOD
    # -----------------------------------------------------

    def add_food(self, order):

        if order is None:
            print("Create an order first.")
            return

        try:

            food_id = int(input("Food ID: "))
            food = self.find_food(food_id)

            if not food:
                print("Invalid food ID.")
                return

            portion = None

            if food.portions:

                print("\nPortion")

                options = list(food.portions.keys())

                for i, p in enumerate(options, 1):
                    print(f"{i}. {p} - ₹{food.portions[p]}")

                while True:

                    try:
                        p_choice = int(input("Choose portion: "))

                        if 1 <= p_choice <= len(options):
                            portion = options[p_choice - 1]
                            break

                        print("Invalid choice.")

                    except ValueError:
                        print("Enter a number.")

            quantity = int(input("Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

            order.add_item(food, quantity, portion)

            print("Item added to cart.")

        except ValueError:
            print("Please enter valid numbers.")

    # -----------------------------------------------------
    # REMOVE FOOD
    # -----------------------------------------------------

    def remove_food(self, order):

        if order is None or not order.items:
            print("Cart is empty.")
            return

        print("\nItems in cart:")

        keys = list(order.items.keys())

        for i, key in enumerate(keys, 1):

            item = order.items[key]

            portion = (
                f" ({item['portion']})"
                if item["portion"] else ""
            )

            print(
                f"{i}. {item['food'].name}"
                f"{portion} - Qty {item['quantity']}"
            )

        try:

            choice = int(input("Choose item: "))

            if not 1 <= choice <= len(keys):
                print("Invalid choice.")
                return

            key = keys[choice - 1]

            quantity = int(
                input("Quantity to remove: ")
            )

            if quantity <= 0:
                print("Invalid quantity.")
                return

            order.remove_item(key, quantity)

            print("Item removed.")

        except ValueError:
            print("Enter valid numbers.")

    # -----------------------------------------------------
    # CHECKOUT
    # -----------------------------------------------------

    def checkout(self, order):

        if order is None or not order.items:
            print("No items in cart.")
            return False

        subtotal = order.subtotal()

        # Discount
        if subtotal >= 500:
            discount = subtotal * 0.10
        elif subtotal >= 300:
            discount = subtotal * 0.05
        else:
            discount = 0

        delivery = 0

        if order.order_type == "Online Delivery":

            if subtotal < 300:
                delivery = 50
            elif subtotal < 500:
                delivery = 40
            else:
                delivery = 0

        print("\nPayment Method")

        if order.order_type == "Online Delivery":
            print("1. UPI")
            print("2. Card")
            print("3. Cash on Delivery")
        else:
            print("1. Cash")
            print("2. UPI")
            print("3. Card")

        while True:

            choice = input("Choose payment method: ")

            if order.order_type == "Online Delivery":

                methods = {
                    "1": "UPI",
                    "2": "Card",
                    "3": "Cash on Delivery"
                }

            else:

                methods = {
                    "1": "Cash",
                    "2": "UPI",
                    "3": "Card"
                }

            if choice in methods:
                payment = methods[choice]
                break

            print("Invalid choice.")

        total = subtotal - discount + delivery

        # Payment confirmation
        print("\nProcessing payment...")

        if payment != "Cash on Delivery":
            print("Payment successful!")

        # -------------------------------------------------
        # DETAILED SUMMARY
        # -------------------------------------------------

        print("\n" + "=" * 70)
        print("                         SWADH")
        print("                    ORDER SUMMARY")
        print("=" * 70)

        print(f"Customer      : {order.customer}")
        print(f"Token Number  : {order.token}")
        print(f"Order Type    : {order.order_type}")
        print(
            f"Date & Time   : "
            f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
        )

        if order.order_type == "Dine-in":
            print(f"Table Number  : {order.table}")

        elif order.order_type == "Online Delivery":
            print(f"Phone         : {order.phone}")
            print(f"Address       : {order.address}")

        print("-" * 70)

        for item in order.items.values():

            portion = (
                f" ({item['portion']})"
                if item["portion"]
                else ""
            )

            amount = item["price"] * item["quantity"]

            print(
                f"{item['food'].name}{portion:<10} "
                f"{item['quantity']} x ₹{item['price']}"
                f" = ₹{amount}"
            )

        print("-" * 70)

        print(f"Subtotal         : ₹{subtotal:.2f}")
        print(f"Discount          : ₹{discount:.2f}")

        if order.order_type == "Online Delivery":

            if delivery == 0:
                print("Delivery Charge   : FREE")
            else:
                print(f"Delivery Charge   : ₹{delivery:.2f}")

        print(f"TOTAL PAID        : ₹{total:.2f}")
        print(f"Payment Method    : {payment}")
        print(f"Waiting Time      : {order.waiting_time()} minutes")

        if order.order_type == "Online Delivery":
            print("Order Status      : Confirmed")
        else:
            print("Order Status      : Confirmed")

        print("=" * 70)
        print("             Thank you for ordering from SWADH!")
        print("=" * 70)

        self.save_order(
            order,
            subtotal,
            discount,
            delivery,
            total,
            payment
        )

        return True

    # -----------------------------------------------------
    # SAVE CSV + RECEIPT
    # -----------------------------------------------------

    def save_order(
        self,
        order,
        subtotal,
        discount,
        delivery,
        total,
        payment
    ):

        # CSV
        with open(
            "orders.csv",
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            if file.tell() == 0:

                writer.writerow([
                    "Date",
                    "Token",
                    "Customer",
                    "Order Type",
                    "Items",
                    "Subtotal",
                    "Discount",
                    "Delivery",
                    "Total",
                    "Payment"
                ])

            items_text = ""

            for item in order.items.values():

                portion = (
                    f" ({item['portion']})"
                    if item["portion"]
                    else ""
                )

                items_text += (
                    f"{item['food'].name}{portion} "
                    f"x{item['quantity']}; "
                )

            writer.writerow([
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                order.token,
                order.customer,
                order.order_type,
                items_text,
                subtotal,
                discount,
                delivery,
                total,
                payment
            ])

        # TXT receipt
        filename = f"receipt_{order.token}.txt"

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("SWADH\n")
            file.write("ORDER RECEIPT\n")
            file.write("=" * 50 + "\n")

            file.write(
                f"Customer: {order.customer}\n"
            )
            file.write(
                f"Token: {order.token}\n"
            )
            file.write(
                f"Order Type: {order.order_type}\n"
            )

            file.write(
                f"Date: "
                f"{datetime.now().strftime('%d-%m-%Y %I:%M %p')}\n"
            )

            if order.table:
                file.write(
                    f"Table: {order.table}\n"
                )

            if order.address:
                file.write(
                    f"Address: {order.address}\n"
                )

            file.write("-" * 50 + "\n")

            for item in order.items.values():

                portion = (
                    f" ({item['portion']})"
                    if item["portion"]
                    else ""
                )

                amount = item["price"] * item["quantity"]

                file.write(
                    f"{item['food'].name}{portion} "
                    f"x{item['quantity']} = ₹{amount}\n"
                )

            file.write("-" * 50 + "\n")

            file.write(
                f"Subtotal: ₹{subtotal:.2f}\n"
            )
            file.write(
                f"Discount: ₹{discount:.2f}\n"
            )
            file.write(
                f"Delivery: ₹{delivery:.2f}\n"
            )
            file.write(
                f"TOTAL: ₹{total:.2f}\n"
            )
            file.write(
                f"Payment: {payment}\n"
            )
            file.write(
                f"Waiting Time: "
                f"{order.waiting_time()} minutes\n"
            )

            file.write("=" * 50 + "\n")
            file.write("Thank you for choosing SWADH!\n")

        print(
            f"\nReceipt saved as {filename}"
        )

    # -----------------------------------------------------
    # PREVIOUS ORDERS
    # -----------------------------------------------------

    def previous_orders(self):

        try:

            with open(
                "orders.csv",
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)
                orders = list(reader)

                if not orders:
                    print("No previous orders.")
                    return

                print("\n" + "=" * 80)
                print("PREVIOUS ORDERS")
                print("=" * 80)

                for order in orders:

                    print(
                        f"Token: {order['Token']} | "
                        f"Customer: {order['Customer']} | "
                        f"Type: {order['Order Type']}"
                    )

                    print(
                        f"Total: ₹{order['Total']} | "
                        f"Payment: {order['Payment']}"
                    )

                    print(
                        f"Items: {order['Items']}"
                    )

                    print("-" * 80)

        except FileNotFoundError:

            print("No previous orders found.")

    # -----------------------------------------------------
    # STATISTICS
    # -----------------------------------------------------

    def statistics(self):

        try:

            with open(
                "orders.csv",
                "r",
                encoding="utf-8"
            ) as file:

                orders = list(csv.DictReader(file))

                if not orders:
                    print("No order data.")
                    return

                total_sales = sum(
                    float(order["Total"])
                    for order in orders
                )

                print("\n" + "=" * 45)
                print("SWADH RESTAURANT STATISTICS")
                print("=" * 45)

                print(
                    f"Total Orders : {len(orders)}"
                )

                print(
                    f"Total Sales  : ₹{total_sales:.2f}"
                )

                print(
                    f"Average Order: "
                    f"₹{total_sales / len(orders):.2f}"
                )

                print("=" * 45)

        except FileNotFoundError:

            print("No order data available.")


# =========================================================
# MAIN
# =========================================================

def main():

    restaurant = Restaurant()
    current_order = None

    while True:

        print("\n")
        print("=" * 50)
        print("             WELCOME TO SWADH")
        print("=" * 50)

        print("1. View Menu")
        print("2. Search Food")
        print("3. View Categories")
        print("4. Create New Order")
        print("5. Add Food")
        print("6. View Cart")
        print("7. Remove Food")
        print("8. Checkout / Pay")
        print("9. Previous Orders")
        print("10. Restaurant Statistics")
        print("11. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            restaurant.show_menu()

        elif choice == "2":

            restaurant.search()

        elif choice == "3":

            print("\nCategories:")

            for category in restaurant.categories:
                print("-", category)

        elif choice == "4":

            current_order = restaurant.create_order()

        elif choice == "5":

            restaurant.add_food(current_order)

        elif choice == "6":

            if current_order:
                current_order.show_cart()
            else:
                print("Create an order first.")

        elif choice == "7":

            restaurant.remove_food(current_order)

        elif choice == "8":

            if restaurant.checkout(current_order):
                current_order = None

        elif choice == "9":

            restaurant.previous_orders()

        elif choice == "10":

            restaurant.statistics()

        elif choice == "11":

            print("\nThank you for visiting SWADH!")
            break

        else:

            print(
                "Invalid choice. "
                "Please enter 1-11."
            )


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":
    main()