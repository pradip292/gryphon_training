def calculate_total_cost(cart_items):
    return sum(item['price'] * item['quantity'] for item in cart_items)

