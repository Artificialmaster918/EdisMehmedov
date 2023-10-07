age = int(input())
if age < 18:
    print("You are a minor")
elif age >= int(18) and age < int(65):
    print("You are an adult")
else:
    print("You are a senior citizen")