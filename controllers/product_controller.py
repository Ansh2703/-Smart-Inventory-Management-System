from models.product import Product

class ProductController:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, category, price, stock, reorder_threshold, app):
        product = Product(product_id, name, category, price, stock, reorder_threshold, app)
        self.products[product_id] = product
        return product

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def update_product_stock(self, product_id, quantity):
        product = self.get_product(product_id)
        if product:
            product.update_stock(quantity)

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
