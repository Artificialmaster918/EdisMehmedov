# · Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# · Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;
# · Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# · Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# · Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
flower_type = input()  # "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
flower_count = int(input())
budget = int(input())

flower_price = 0
discount = 0
if flower_type == "Roses":
    flower_price = 5
    if flower_count > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    flower_price = 3.80
    if flower_count > 90:
        discount = 0.15
elif flower_type == "Tulips":
    flower_price = 2.80
    if flower_count > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    flower_price = 3
    if flower_count < 120:
        discount = -0.15
elif flower_type == "Gladiolus":  # eq: else IF valid input is guaranteed
    flower_price = 2.50
    if flower_count < 80:
        discount = -0.20

total_cost = flower_count * flower_price * (1 - discount)
if budget >= total_cost:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - total_cost :.2f} leva left.")

elif total_cost > budget:
    print(f"Not enough money, you need {total_cost - budget :.2f} leva more.")
