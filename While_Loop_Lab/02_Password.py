username = input()
correct_password = input()
new_password = input()
# Докато новата парола не е същата като правилната
while new_password != correct_password:
    new_password = input()
print(f"Welcome {username}!")