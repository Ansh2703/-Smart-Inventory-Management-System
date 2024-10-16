class Warehouse:
    def __init__(self, warehouse_id, location):
        self.warehouse_id = warehouse_id
        self.location = location
        self.products = {}

    def add_product(self, product, quantity):
        if product.product_id in self.products:
            self.products[product.product_id].update_stock(quantity)
        else:
            self.products[product.product_id] = product
            

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def __str__(self):
        return f"Warehouse({self.location}) | Products: {len(self.products)}"
