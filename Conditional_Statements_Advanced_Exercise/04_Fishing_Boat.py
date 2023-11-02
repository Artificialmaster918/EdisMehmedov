budget = int(input())
season = input()
fishermans = int(input())
price = 0
discount = 0
extra_discount = 0
if season == "Spring":
    price = 3000

elif season == "Summer" or season == "Autumn":
    price = 4200

elif season == "Winter":
    price = 2600


if fishermans <= 6:
    discount = 0.10
elif fishermans <= 11:
    discount = 0.15
else:
    discount = 0.25

if fishermans % 2 == 0 and season != "Autumn":
    extra_discount = 0.05


ammount = price * (1 - discount) * (1-extra_discount)
if ammount <= budget:
    print(f"Yes! You have {budget - ammount:.2f} leva left.")
else:
    print(f"Not enough money! You need {ammount - budget:.2f} leva.")