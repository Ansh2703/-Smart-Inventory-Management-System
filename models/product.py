from tkinter import messagebox

class Product:
    def __init__(self, product_id, name, category, price, stock, reorder_threshold=10, app=None):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.reorder_threshold = reorder_threshold
        self.app = app  # Reference to the main application

    def update_stock(self, quantity):
        self.stock += quantity
        if self.stock <= self.reorder_threshold:
            self.reorder()

    def reorder(self):
        # Show a popup message when the stock is low
        if self.app:
            messagebox.showwarning("Low Stock", f"Reordering product '{self.name}' due to low stock!")

    def __str__(self):
        return f"{self.name} | {self.category} | Stock: {self.stock} | Price: {self.price}"
