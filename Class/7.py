class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, **kwargs):
        """Add product to the cart."""
        self.items_in_cart.update(kwargs)
        print "%s added." % kwargs

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart('Tasneem')
my_cart.add_item(**{'soap': 18, 'shoe': 200})
my_cart.remove_item('soap')