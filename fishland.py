mackerel_pricekg = float(input())
sprat_pricekg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

palamud_pricekg = mackerel_pricekg + mackerel_pricekg * 0.60
palamud_final = palamud_kg * palamud_pricekg

safrid_pricekg = sprat_pricekg + sprat_pricekg * 0.80
safrid_final = safrid_kg * safrid_pricekg

mussels_final = mussels_kg * 7.50

price = palamud_final + safrid_final + mussels_final
finalprice = round(price, 2)
print(finalprice)