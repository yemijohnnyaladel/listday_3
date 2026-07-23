prices = {"Bread": 50, "Milk": 80}

discounted = {item: p * 0.9 for item, p in prices.items()}

print(discounted)