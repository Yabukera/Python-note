def calculate_total():
    adult_price = "25"
    child_price = 12
    discount = 5
    
    adults = 3
    children = 2
    
    total = (adult_price * adults) + (child_price * children)
    final_total = total - discount
    
    print("Final Price: $" + str(final_total))

calculate_total()

