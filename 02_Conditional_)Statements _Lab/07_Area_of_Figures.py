#type_of_figure = str(square, rectangle, circle или triangle))
from Conditional_Statements_Exercise import math

figure = input()

if figure == "square":
    side = a = float(input())  # да ни пита за страната
    area = a * a
    format_result = "{:.3f}".format(area)
    print(format_result)
elif figure == "rectangle":
    result2 = a = float(input())
    result22 = b = float(input())
    result222 = a * b
    format_result2 = "{:.3f}".format(result222)
    print(format_result2)
elif figure == "circle":
    result3 = r = float(input())
    result33 = math.pi * pow(r, 2)
    format_result3 = "{:.3f}".format(result33)
    print(format_result3)
elif figure == "triangle":
    result4 = a = float(input())
    result_h = h = float(input())
    result44 = a * h / 2
    format_res4 = "{:.3f}".format(result44)
    print(format_res4)