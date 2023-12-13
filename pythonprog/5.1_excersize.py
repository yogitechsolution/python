#Price of house 1m
#If buyer has good credit
    #Need to put down payment 10%
#otherwaise
    #Need to put down payment 20%
#print down paymnet

price = 1_000_000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print("Down Payment: " + str(down_payment))
print(f"Down Payment: ${down_payment}")

