# match case in python
amount = float (input ("Enter amount: "))
discount = 0
if amount > 5000:
    discount = 0.2
elif amount >= 3000:
    discount = 0.1
final_price  = amount - discount
print("Final Price:", final_price)