# discount.py

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies the discount if it's 20% or higher.
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative.")
    
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return round(final_price, 2)
    else:
        return price
