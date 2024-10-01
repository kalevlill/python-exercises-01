def price_with_tax(price):
    tax_rate = 0.19 # MWS von 19 %
    total_price = price * (1 + tax_rate)
    return total_price

net_price = 99,99
total_price = price_with_tax(net_price)
print(f"Der Gesamtpreis inklusive 19 % MWS beträgt: {total_price:.2f} €")
