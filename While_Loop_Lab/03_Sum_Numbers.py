control_number = int(input())
sum_of_numbers = 0
# докато тяхната сума e по-малка на първоначалното число чета нов вход
while sum_of_numbers < control_number:
    current_number = int(input())
    sum_of_numbers += current_number
print(sum_of_numbers)