import numpy as np

prices = np.array([200,400,500,700])
discount = 10

finalPrize = prices - (prices * discount/100)

print(prices)
print(finalPrize)