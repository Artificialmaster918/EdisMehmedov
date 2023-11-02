budget = float(input())
season = input()

where = ""
hotel_or_camp = ""
if budget <= 100:
    where = "Bulgaria"
    if season == "summer":
        budget *= 0.30
        hotel_or_camp = "Camp"
    elif season == "winter":
        budget *= 0.70
        hotel_or_camp = "Hotel"
elif 100 < budget <= 1000:
    where = "Balkans"
    if season == "summer":
        budget *= 0.40
        hotel_or_camp = "Camp"
    elif season == "winter":
        budget *= 0.80
        hotel_or_camp = "Hotel"
elif budget > 1000:
    where = "Europe"
    if season == "summer":
        budget *= 0.90
        hotel_or_camp = "Hotel"
    elif season == "winter":
        budget *= 0.90
        hotel_or_camp = "Hotel"



print(f"Somewhere in {where}")
print(f"{hotel_or_camp} - {budget:.2f}")