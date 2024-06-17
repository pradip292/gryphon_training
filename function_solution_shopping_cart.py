def calculate_total_cost(cart_items):
    return sum(item['price'] * item['quantity'] for item in cart_items)

def main():
    shopping_cart = [
        {'item': 'Laptop', 'price': 1200.0, 'quantity': 2},
        {'item': 'Headphones', 'price': 50.0, 'quantity': 3},
        {'item': 'Mouse', 'price': 20.0, 'quantity': 1}
    ]
    result = calculate_total_cost(shopping_cart)
    print(f"Total cost of items in the shopping cart: ${result:.2f}")

