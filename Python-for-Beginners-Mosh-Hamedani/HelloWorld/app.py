# house: 1M $
# if the buyer has good credit, they will need to put down 10 percent of the price of this property
# otherwise they need to put down 20 percent
# display payment
price = 1000000
has_good_credit = True

if has_good_credit:
    price = price - (price * 0.1)
else:
    price = price - (price * 0.2)

print(f"Payment: {price}")