count_of_numbers = int(input())
total_sum = 0
for numbers in range(count_of_numbers):  # range(0, count_of_numbers) #range(1, count_of_numbers + 1)
    current_number = int(input())
    total_sum += current_number
print(total_sum)