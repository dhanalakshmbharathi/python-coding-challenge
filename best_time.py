prices=[7,1,5,3,6,4]
# max_profit=-1234567890
# profit=-1234567
# for buy in range(len(prices)):
#     for sell in range(buy+1,len(prices)):
#         profit=prices[sell]-prices[buy]
#         max_profit=max(max_profit,profit)
# if max_profit<0:
#     print(max_profit) 
# else:
#     print(max_profit)     
max_profit=0
profit=0
for i in range(1,len(prices)):
    profit=max(0,profit+prices[i]-prices[i-1])
    max_profit=max(max_profit,profit)
print(max_profit)
        