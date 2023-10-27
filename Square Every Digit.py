def dis(price, discount):
    sum = price - (discount * (price/100))
    return round(sum)


print(dis(87.527, 20))
