def calculate_total_cost(cart_items):
    total_cost = 0
    for item in cart_items:
        total_cost += item['price'] * item['quantity']
    return total_cost

