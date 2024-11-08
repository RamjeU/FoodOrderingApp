# Food Ordering App 🥘

A simple food ordering application built with Python and Tkinter that allows users to select items from a menu, manage a shopping cart, and simulate a payment process.

## Features

### Main Application (`FoodOrderingApp.py`)
- **Interactive Menu**: Browse through items, view descriptions, and prices.
- **Shopping Cart**: Add items to the cart, update quantities, or remove items.
- **Order Summary**: View the total cost of items in the cart.
- **User-Friendly Design**: Built with Tkinter for an intuitive graphical interface.

### Payment System (`Payment.py`)
- **Mock Payment Gateway**: Users can simulate a payment by entering fake payment details.
- **Validation**: Ensures all payment fields are filled correctly.
- **Integration**: Works seamlessly with the main application to confirm orders.

Screenshots 🖼️
Menu Page


Cart Page
<!-- Replace with your screenshot path -->

---

## How to Use

1. **Run the Main Application**:
   - Open the terminal or command prompt and run:
     ```bash
     python FoodOrderingApp.py
     ```

2. **Place an Order**:
   - Browse the menu, select items, and add them to your cart.
   - Click on "Checkout" when ready.

3. **Simulate Payment**:
   - A payment window will pop up.
   - Enter the following test details to confirm payment:
     - **Card Number**: `1234 5678 8765 4321`
     - **Expiry Date**: `12/34`
     - **CVV**: `123`
   - Click "Confirm Payment" to place your order.

4. **Order Confirmation**:
   - After payment, your cart will be cleared, and the app will confirm the order.

---

## Future Plans

- **Database Integration**: Use MongoDB to store menu items, orders, and user data.
- **Web Application**: Convert the project into a Django-based website for wider accessibility.
- **Dynamic Menu Updates**: Integrate APIs to fetch and update menu items automatically.
- **Real Payment Gateway**: Replace mock payment with a real service like Stripe or PayPal.

---

## Author

Ramje Uthayakumaar 

Feel free to reach out for feedback or suggestions!
--- 
