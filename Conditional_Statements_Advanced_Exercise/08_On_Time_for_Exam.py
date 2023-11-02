exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_total_minutes = exam_hour * 60 + exam_minute
arrive_total_minutes = arrive_hour * 60 + arrive_minute

if arrive_total_minutes > exam_total_minutes:
    print("Late")
elif exam_total_minutes - arrive_total_minutes <= 30:
    print("On time")
else:
    print("Early")

result = abs(exam_total_minutes - arrive_total_minutes)
if exam_total_minutes - arrive_total_minutes > 0:
    if result < 60:
        print(f"{result} minutes before the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours before the start")
elif arrive_total_minutes - exam_total_minutes > 0:
    if result < 60:
        print(f"{result} minutes after the start")
    else:
        print(f"{result // 60}:{result % 60:02d} hours after the start")

# exam_hours = int(input())
# exam_minutes = int(input())
# arrival_hours = int(input())
# arrival_minutes = int(input())
#
# total_exam_min = exam_hours * 60 + exam_minutes
# total_arrival_min = arrival_hours * 60 + arrival_minutes
# hours_left = 0
# min_left = 0
#
# diff = abs(total_exam_min - total_arrival_min)
#
# if total_arrival_min > total_exam_min:
#     print("Late")
#     if diff >= 60:
#         hours_left = diff // 60
#         min_left = diff % 60
#         if min_left < 10:
#             print(f"{hours_left}:0{min_left} hours after the start")
#         else:
#             print(f"{hours_left}:{min_left} hours after the start")
#     else:
#         if diff < 10:
#             print(f"0{diff} minutes after the start")
#         else:
#             print(f"{diff} minutes after the start")
# elif total_arrival_min == total_exam_min:
#     print("On time")
#
# elif total_arrival_min < total_exam_min:
#     if diff <= 30:
#         print("On time")
#         print(f"{diff} minutes before the start")
#     else:
#         if diff >= 60:
#             hours_left = diff // 60
#             min_left = diff % 60
#             if min_left < 10:
#                 print("Early")
#                 print(f"{hours_left}:0{min_left} hours before the start")
#             else:
#                 print("Early")
#                 print(f"{hours_left}:{min_left} hours before the start")
#         else:
#             print("Early")
#             print(f"{diff} minutes before the start")