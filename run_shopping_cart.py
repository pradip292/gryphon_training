from loop_solution_shopping_cart import calculate_total_cost as loop_calculate_total_cost
from method_solution_shopping_cart import calculate_total_cost as method_calculate_total_cost
from function_solution_shopping_cart import calculate_total_cost as function_calculate_total_cost, main as function_main

if __name__ == "__main__":
    shopping_cart = [
        {'item': 'Laptop', 'price': 1200.0, 'quantity': 2},
        {'item': 'Headphones', 'price': 50.0, 'quantity': 3},
        {'item': 'Mouse', 'price': 20.0, 'quantity': 1}
    ]

   
    loop_result = loop_calculate_total_cost(shopping_cart)
    print(f"Total cost using loops: ${loop_result:.2f}")

    
    method_result = method_calculate_total_cost(shopping_cart)
    print(f"Total cost using methods: ${method_result:.2f}")

 
    function_result = function_calculate_total_cost(shopping_cart)
    print(f"Total cost using functions: ${function_result:.2f}")

   
    function_main()
