import tkinter as tk
from tkinter import ttk, messagebox

class PaymentWindow:
    def __init__(self, root, total_amount, on_payment_success):
        self.root = tk.Toplevel(root)
        self.root.title("Payment")
        self.total_amount = total_amount
        self.on_payment_success = on_payment_success

        # Payment form title
        ttk.Label(self.root, text="Payment Information", font=("TkDefaultFont", 14, "bold")).pack(pady=10)

        # Total amount display
        ttk.Label(self.root, text=f"Total Amount: ${self.total_amount:.2f}", font=("TkDefaultFont", 12)).pack(pady=5)

        # Card Number field
        ttk.Label(self.root, text="Card Number:").pack(anchor="w", padx=10)
        self.card_number_entry = ttk.Entry(self.root)
        self.card_number_entry.pack(fill="x", padx=10, pady=5)

        # Expiration Date field
        ttk.Label(self.root, text="Expiration Date (MM/YY):").pack(anchor="w", padx=10)
        self.expiry_date_entry = ttk.Entry(self.root)
        self.expiry_date_entry.pack(fill="x", padx=10, pady=5)

        # CVV field
        ttk.Label(self.root, text="CVV:").pack(anchor="w", padx=10)
        self.cvv_entry = ttk.Entry(self.root, show="*")
        self.cvv_entry.pack(fill="x", padx=10, pady=5)

        # Payment button
        ttk.Button(self.root, text="Confirm Payment", command=self.process_payment).pack(pady=15)

    def process_payment(self):
        # Get card details
        card_number = self.card_number_entry.get()
        expiry_date = self.expiry_date_entry.get()
        cvv = self.cvv_entry.get()

        # Validate fields (just check if not empty in this example)
        if not card_number or not expiry_date or not cvv:
            messagebox.showerror("Error", "All fields are required")
            return

        # Mock payment processing logic
        if card_number == "1234 5678 8765 4321" and expiry_date == "12/34" and cvv == "123":
            messagebox.showinfo("Success", "Payment successful!")
            self.on_payment_success()
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid payment details. This is a mock payment, try 1234 5678 8765 4321 with expiry 12/34 and CVV 123.")

# Usage example
if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentWindow(root, 100, lambda: print("Payment was successful!"))
    root.mainloop()
