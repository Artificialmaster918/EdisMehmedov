from Conditional_Statements_Exercise import math

figure = input()

if figure == "square":
    a = float(input())
    area_square = a * a
    print(f"{area_square:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area_rectangle = a * b
    print(f"{area_rectangle:.3f}")
elif figure == "circle":
    r = float(input())
    area_circle = math.pi * r * r
    print(f"{area_circle:.3f}")
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area_triangle = a * h / 2
    print(f"{area_triangle:.3f}")