
price1 = input("Enter the price of the item: ")
price = float(price1)
discount_percent1 = input("Enter the discount percentage: ")
discount_percent = float(discount_percent1)

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # check the percentage, not the discounted price
        final_price = price - (price * discount_percent) / 100
        print(f"Discounted price: {final_price}")
    else:
        print(f"Price: {price}")

calculate_discount(price, discount_percent)  