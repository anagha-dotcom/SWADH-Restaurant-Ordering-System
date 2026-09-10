# 🍽️ SWADH – Restaurant Ordering System

A **menu-driven Python mini project** developed using **Object-Oriented Programming (OOP)** concepts. SWADH simulates a real-world restaurant ordering system with menu management, cart handling, multiple order types, payment options, discounts, delivery charges, order history, statistics, and receipt generation.

## 📌 Project Overview

SWADH allows customers to:

* View the restaurant menu
* Search for food items
* View food categories
* Create a new order
* Add and remove food items
* Select food portions where applicable
* Choose an order type
* Apply discounts automatically
* Calculate delivery charges
* Select a payment method
* Generate a detailed order receipt
* View previous orders
* View restaurant statistics

## ✨ Features

### 🍛 Menu Categories

* Lunch
* Chinese
* Mandhi
* Drinks
* Desserts

### 🛍️ Ordering

* Dine-in
* Takeaway
* Online Delivery
* Half / Full portions for selected items
* Add items to cart
* Remove items from cart
* Quantity management

### 💰 Billing

* 5% discount for orders of ₹300 or more
* 10% discount for orders of ₹500 or more
* Delivery charges based on order value
* Multiple payment options

### 💳 Payment Methods

**Dine-in / Takeaway**

* Cash
* UPI
* Card

**Online Delivery**

* UPI
* Card
* Cash on Delivery

### 📄 File Handling

The program uses:

* **CSV** file to store order history
* **TXT** files to generate individual order receipts

### 📊 Additional Features

* Food search
* Previous order history
* Restaurant sales statistics
* Order token numbers
* Estimated waiting time
* Invalid input handling

## 🧑‍💻 OOP Concepts Used

The project demonstrates the following OOP concepts:

* Classes
* Objects
* Constructors
* Instance variables
* Methods

### Main Classes

**FoodItem**

* Stores food ID, name, category, price, and portion information.

**Order**

* Handles customer details, order type, cart items, quantities, and order calculations.

**Restaurant**

* Manages the menu, orders, checkout, file handling, previous orders, and statistics.

## 🐍 Python Concepts Demonstrated

This project covers the major concepts learned during Week 1:

* Variables
* Conditional statements
* `if`, `elif`, `else`
* `for` loops
* `while` loops
* Functions
* Lists
* Tuples
* Sets
* Dictionaries
* Exception handling
* File handling
* Object-Oriented Programming

## 📂 Project Structure

```text
SWADH-Restaurant-Ordering-System/
│
├── resturant_ordering.py
└── README.md
```

The program automatically creates:

```text
orders.csv
receipt_1001.txt
receipt_1002.txt
...
```

when orders are placed.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project folder

```bash
cd SWADH-Restaurant-Ordering-System
```

### 3. Run the program

```bash
python resturant_ordering.py
```

## 🖥️ Main Menu

The application provides options such as:

```text
1. View Menu
2. Search Food
3. View Categories
4. Create New Order
5. Add Food
6. View Cart
7. Remove Food
8. Checkout / Pay
9. Previous Orders
10. Restaurant Statistics
11. Exit
```

## 🎯 Objective

The main objective of this project is to demonstrate the practical implementation of **Python programming and Object-Oriented Programming concepts** by developing a functional restaurant ordering application.

## 👩‍💻 Technologies Used

* Python
* Object-Oriented Programming
* CSV File Handling
* TXT File Handling

## 🚀 Future Enhancements

Possible future improvements include:

* Graphical User Interface
* Database integration
* Online payment integration
* User login and registration
* Real-time order status
* Admin dashboard
* Inventory management

## 📜 License

This project was created for **educational purposes** as part of a Python mini project.
