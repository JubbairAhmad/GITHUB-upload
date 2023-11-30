prices = list(map(int,input().split(' ')))
profit = 0
buy = prices[0]
for sell in prices[1:]:
    if sell > buy:
        profit = max(profit, sell - buy)
    else:
        buy = sell
        
print(profit)