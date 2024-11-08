import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict
from payment import PaymentWindow



class FoodOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Ordering System")
        self.root.geometry("1000x600")

        # Menu items with prices and descriptions
        self.menu = {
            "Margherita Pizza": {"price": 12.99, "description": "Classic tomato and mozzarella"},
            "Chicken Burger": {"price": 8.99, "description": "Grilled chicken with lettuce and mayo"},
            "Caesar Salad": {"price": 7.99, "description": "Fresh romaine lettuce with Caesar dressing"},
            "French Fries": {"price": 4.99, "description": "Crispy golden fries"},
            "Coca Cola": {"price": 2.99, "description": "Classic cold drink"},
            "Chocolate Ice Cream": {"price": 5.99, "description": "Rich chocolate flavor"}
        }

        self.cart: Dict[str, dict] = {}
        self.total = 0.0

        self.create_widgets()

    def create_widgets(self):
        # Main container
        main_container = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Left side (Menu)
        left_frame = ttk.LabelFrame(main_container, text="Menu", padding="10")
        main_container.add(left_frame, weight=1)

        # Right side (Cart)
        right_frame = ttk.LabelFrame(main_container, text="Shopping Cart", padding="10")
        main_container.add(right_frame, weight=1)

        # Create menu items
        self.create_menu_section(left_frame)

        # Create cart section
        self.create_cart_section(right_frame)

    def create_menu_section(self, parent):
        # Canvas for scrolling
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Menu items
        for idx, (item, details) in enumerate(self.menu.items()):
            # Item frame
            item_frame = ttk.Frame(scrollable_frame)
            item_frame.pack(fill="x", padx=5, pady=5)

            # Item name (bold)
            name_label = ttk.Label(item_frame, text=item, style="Bold.TLabel")
            name_label.grid(row=0, column=0, sticky="w")

            # Price
            price_label = ttk.Label(item_frame, text=f"${details['price']:.2f}")
            price_label.grid(row=0, column=1, padx=10)

            # Description
            desc_label = ttk.Label(item_frame, text=details['description'])
            desc_label.grid(row=1, column=0, columnspan=2, sticky="w")

            # Quantity selector
            qty_var = tk.StringVar(value="1")
            qty_spinbox = ttk.Spinbox(
                item_frame,
                from_=1,
                to=10,
                width=5,
                textvariable=qty_var
            )
            qty_spinbox.grid(row=0, column=2, padx=5)

            # Add to cart button
            add_btn = ttk.Button(
                item_frame,
                text="Add to Cart",
                command=lambda i=item, q=qty_var: self.add_to_cart(i, q)
            )
            add_btn.grid(row=0, column=3, padx=5)

            # Separator
            ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=5)

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def create_cart_section(self, parent):
        # Cart contents will be displayed in a treeview
        self.cart_tree = ttk.Treeview(
            parent,
            columns=("Item", "Quantity", "Price", "Subtotal"),
            show="headings",
            height=10
        )

        # Configure columns
        self.cart_tree.heading("Item", text="Item")
        self.cart_tree.heading("Quantity", text="Quantity")
        self.cart_tree.heading("Price", text="Price")
        self.cart_tree.heading("Subtotal", text="Subtotal")

        # Set column widths
        self.cart_tree.column("Item", width=150)
        self.cart_tree.column("Quantity", width=70)
        self.cart_tree.column("Price", width=70)
        self.cart_tree.column("Subtotal", width=70)

        self.cart_tree.pack(fill="both", expand=True, pady=5)

        # Buttons frame
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill="x", pady=5)

        ttk.Button(btn_frame, text="Remove Selected", command=self.remove_from_cart).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear Cart", command=self.clear_cart).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Checkout", command=self.checkout).pack(side="right", padx=5)

        # Total label
        self.total_label = ttk.Label(parent, text="Total: $0.00", font=("TkDefaultFont", 12, "bold"))
        self.total_label.pack(side="right", pady=10)

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

    def remove_from_cart(self):
        selected_item = self.cart_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to remove")
            return

        item = self.cart_tree.item(selected_item)["values"][0]
        del self.cart[item]
        self.update_cart_display()

    def clear_cart(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear the cart?"):
            self.cart.clear()
            self.update_cart_display()

    def update_cart_display(self):
        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)

        self.total = 0.0
        for item, details in self.cart.items():
            subtotal = details["price"] * details["quantity"]
            self.total += subtotal
            self.cart_tree.insert(
                "",
                "end",
                values=(
                    item,
                    details["quantity"],
                    f"${details['price']:.2f}",
                    f"${subtotal:.2f}"
                )
            )

        self.total_label.config(text=f"Total: ${self.total:.2f}")

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Warning", "Your cart is empty!")
            return

            # Open the payment window
        PaymentWindow(self.root, self.total, self.on_payment_success)

    def on_payment_success(self):
        messagebox.showinfo("Success", "Order placed successfully!")
        self.cart.clear()
        self.update_cart_display()


def main():
    root = tk.Tk()
    # Create a bold style for labels
    style = ttk.Style()
    style.configure("Bold.TLabel", font=("TkDefaultFont", 10, "bold"))

    app = FoodOrderingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()