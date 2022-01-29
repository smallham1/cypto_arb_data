maker_fee = 0.001
taker_fee = 0.001
taker_fee2 = 0.002
arb = 0.00115
coin_price = 0.38
funds = 1500
coin_amount = funds/coin_price
'''fee = (funds*taker_fee)
raw_profit = (coin_amount*arb)
profit_s1 = (coin_amount*arb)-((funds*maker_fee)+(funds*taker_fee))
profit_s2 =  (coin_amount*arb)-((funds*taker_fee2)+(funds*taker_fee))
print('raw profit:', raw_profit)
print('maker, taker:', profit_s1)
print('taker, taker:', profit_s2)
print(coin_amount)'''


x = ((y/coin_price)*x) - ((y*taker_fee)+(y*maker_fee))


