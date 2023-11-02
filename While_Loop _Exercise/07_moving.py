space_width = int(input())
space_length = int(input())
space_heigth = int(input())
space_area = space_heigth * space_width * space_length
command = input()
while command != "Done":
    current_number = int(command)
    space_area -= current_number
    if space_area <= 0:
        break
    command = input()
if space_area <= 0:
    print(f"No more free space! You need {-space_area} Cubic meters more.")
else:
    print(f"{space_area} Cubic meters left.")