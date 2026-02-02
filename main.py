prices=[100,102,101,105,110]

returns=[]
for i in range(1,len(prices)):
    r=(prices[i]-prices[i-1])/prices[i-1]
    returns.append(r)

print("Prices:",prices)
print("Returns:",returns)
print("Average return:",sum(returns)/len(returns))
