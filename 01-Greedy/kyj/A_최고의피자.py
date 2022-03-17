import math

topping_num = int(input())
dou_price, topping_price = map(int, input().split())
dou_cal = int(input())
topping_cal = []

for i in range(topping_num):
    topping_cal.append(int(input()))

price = dou_price
cal = dou_cal
per_cur = cal / price

topping_cal.sort(reverse=True)

for i in range(topping_num):

    per_next = 0
    price += topping_price
    cal += topping_cal[i]

    per_next = cal / price
    if math.trunc(per_cur) > math.trunc(per_next):
        break

    per_cur = per_next

cal = cal - topping_cal[i]
price = price - topping_price
per_next = cal / price
print(math.trunc(per_cur))
