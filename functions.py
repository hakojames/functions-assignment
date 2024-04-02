def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

original_price = int(input("Enter the original price: "))
discount_percentage = int(input("Enter the discount-percentage: "))
final_price = calculate_discount(original_price, discount_percentage)
print("Final Price after Discount:", final_price)