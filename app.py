import tkinter as tk
from tkinter import messagebox
from controllers.product_controller import ProductController
from models.warehouse import Warehouse

# Initialize controllers
product_controller = ProductController()
warehouse = Warehouse(1, "Main Warehouse")

# Main Application
class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Inventory Management System")
        self.geometry("600x400")

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Product Form
        self.product_id_label = tk.Label(self, text="Product ID")
        self.product_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.product_id_entry = tk.Entry(self)
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(self, text="Product Name")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.category_label = tk.Label(self, text="Category")
        self.category_label.grid(row=2, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(self)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)

        self.price_label = tk.Label(self, text="Price")
        self.price_label.grid(row=3, column=0, padx=10, pady=10)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=3, column=1, padx=10, pady=10)

        self.stock_label = tk.Label(self, text="Stock")
        self.stock_label.grid(row=4, column=0, padx=10, pady=10)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.grid(row=4, column=1, padx=10, pady=10)

        self.threshold_label = tk.Label(self, text="Reorder Threshold")
        self.threshold_label.grid(row=5, column=0, padx=10, pady=10)
        self.threshold_entry = tk.Entry(self)
        self.threshold_entry.grid(row=5, column=1, padx=10, pady=10)

        # Buttons for actions
        self.add_button = tk.Button(self, text="Add Product", command=self.add_product)
        self.add_button.grid(row=6, column=0, padx=10, pady=10)

        self.update_stock_button = tk.Button(self, text="Update Stock", command=self.update_stock)
        self.update_stock_button.grid(row=6, column=1, padx=10, pady=10)

        self.remove_button = tk.Button(self, text="Remove Product", command=self.remove_product)
        self.remove_button.grid(row=6, column=2, padx=10, pady=10)

        # Listbox for displaying products
        self.product_listbox = tk.Listbox(self, width=60)
        self.product_listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def add_product(self):
        product_id = int(self.product_id_entry.get())
        name = self.name_entry.get()
        category = self.category_entry.get()
        price = float(self.price_entry.get())
        stock = int(self.stock_entry.get())
        threshold = int(self.threshold_entry.get())

        # Pass the messagebox as a popup for low stock
        product_controller.add_product(product_id, name, category, price, stock, threshold, self)
        warehouse.add_product(product_controller.get_product(product_id), stock)
        self.update_product_listbox()

    def update_stock(self):
        product_id = int(self.product_id_entry.get())
        stock_change = int(self.stock_entry.get())
        product_controller.update_product_stock(product_id, stock_change)
        self.update_product_listbox()

    def remove_product(self):
        product_id = int(self.product_id_entry.get())
        product_controller.remove_product(product_id)
        warehouse.remove_product(product_id)
        self.update_product_listbox()

    def update_product_listbox(self):
        self.product_listbox.delete(0, tk.END)
        for product in product_controller.products.values():
            self.product_listbox.insert(tk.END, str(product))

if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()
