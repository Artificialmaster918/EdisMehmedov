fuel_type = str(input())
liters = float(input())
club_card = str(input())
price = 0

if fuel_type == "Gas":
    if club_card == "Yes":
        gas = liters * 0.85
        if 20 < liters <= 25:
            price = gas - 0.08 * gas
        elif liters > 25:
            price = gas - 0.10 * gas
    else:
        price = liters * 0.93
        if 20 < liters <= 25:
            price = price - 0.08 * price
        elif liters > 25:
            price = price - 0.10 * price
elif fuel_type == "Gasoline":
    if club_card == "Yes":
        gasoline = liters * 2.04
        if 20 < liters <= 25:
            price = gasoline - 0.08 * gasoline
        elif liters > 25:
            price = gasoline - 0.10 * gasoline
    else:
        price = liters * 2.22
        if 20 < liters <= 25:
            price = price - 0.08 * price
        elif liters > 25:
            price = price - 0.10 * price
elif fuel_type == "Diesel":
    if club_card == "Yes":
        diesel = liters * 2.21
        if 20 < liters <= 25:
            price = diesel - 0.08 * diesel
        elif liters > 25:
            price = diesel - 0.10 * diesel
    else:
        price = liters * 2.33
        if 20 < liters <= 25:
            price = price - 0.08 * price
        elif liters > 25:
            price = price - 0.10 * price

if price:
    print(f"{price :.2f} lv.")
