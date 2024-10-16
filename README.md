# Inventory Management System

This is a Python-based **Inventory Management System** using **Tkinter** for the graphical user interface (GUI). The system allows small to medium businesses to manage their inventory, including adding, updating, and removing products, monitoring stock levels, and showing alerts when stock is low.

## Table of Contents
- [Features](#features)
- [How the Software Works](#how-the-software-works)
  - [Adding Products](#adding-products)
  - [Updating Stock](#updating-stock)
  - [Removing Products](#removing-products)
  - [Low Stock Alerts](#low-stock-alerts)

---

## Features

- **Add Products**: Add new products by providing details like Product ID, Name, Category, Price, Stock, and Reorder Threshold.
- **Update Stock**: Update stock levels for existing products by increasing or decreasing the quantity.
- **Remove Products**: Remove products from the inventory by entering the Product ID.
- **Monitor Stock Levels**: Alerts are shown if the stock level is below the reorder threshold.
- **Simple GUI**: The system uses a Tkinter-based GUI for easy interaction.

---

## How the Software Works

### Adding Products
- Users can input product details such as **Product ID**, **Name**, **Category**, **Price**, **Stock**, and **Reorder Threshold** in the appropriate fields.
- When the **Add Product** button is clicked, the product is added to the inventory, and the stock is tracked.
  
### Updating Stock
Users can increase or decrease a product's stock by entering the **Product ID** and specifying the stock change amount (positive for restocking, negative for selling).
- Clicking the **Update Stock** button adjusts the inventory's stock level for the product.

### Removing Products
- Users can remove products from the inventory by entering the **Product ID** and clicking the **Remove Product** button.

### Low Stock Alerts
- Whenever the stock level of a product drops below the defined **Reorder Threshold**, the system automatically triggers a warning popup, alerting the user to reorder the product.

