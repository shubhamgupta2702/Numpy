prices = [100,200,300,400]

discount_Prize = 10

final_Prize = []

for price in prices:
  final_price = price - (price * discount_Prize/100)
  final_Prize.append(final_price)
  
print(final_Prize)