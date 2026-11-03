from datetime import datetime

Subtotal = float(input(" Enter your discount amount "))


TUES = 1
WEDS = 2
DISCOUNT_RATE = 0.1
SALES_TAX_RATE = 0.06

current_date_and_time = datetime.now();
weekday = current_date_and_time.weekday();




# Compute and Print the discount amount
weekday = TUES

if weekday  == TUES or weekday == WEDS: 
    if  Subtotal >= 50:
        discount_amount = Subtotal * DISCOUNT_RATE
        Subtotal = Subtotal - discount_amount
        print(f" Discount amount: ${discount_amount:.2f}")


# Compute and Print the sales tax amount
SALES_TAX_RATE 