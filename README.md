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

## Screenshots 🖼️

### Menu Page
![mainmenu](https://github.com/user-attachments/assets/20736691-3061-40cc-865b-0d4b9374ebc0)

### Cart Page
![itemsincart](https://github.com/user-attachments/assets/7ccd57db-e5e9-4579-ad9d-081868512754)

### Payment Page
![paymentpy](https://github.com/user-attachments/assets/ac98b1c2-47f7-4260-a58a-399e9afc5d19)


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
## Example Code Snippets ✨

    def add_to_cart(self, item: str, qty_var: tk.StringVar):
        try:
            quantity = int(qty_var.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity")
            return

        if item in self.cart:
            self.cart[item]["quantity"] += quantity
        else:
            self.cart[item] = {
                "price": self.menu[item]["price"],
                "quantity": quantity
            }

        self.update_cart_display()
        messagebox.showinfo("Success", f"Added {quantity} {item}(s) to cart!")




---

## Future Plans

- **Database Integration**: Use MongoDB to store menu items, orders, and user data.
- **Web Application**: Convert the project into a Django-based website for wider accessibility.
- **Dynamic Menu Updates**: Integrate APIs to automatically fetch and update menu items.
- **Real Payment Gateway**: Replace mock payment with a real service like Stripe or PayPal.

---
Feel free to reach out for feedback or suggestions!
--- 
