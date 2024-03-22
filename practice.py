print("Enter the missing number:")
print("1. momentum(p)")
print("2. mass(m)")
print("3. velocity(v)")
missing_value_choice = input("Enter the option number for missing value:")
if missing_value_choice == '3':
    p = float(input("Enter momentum(p)"))
    m = float(input("Enter mass(m)"))
    v = p / m
    print(f"velocity(v) = {v}")
elif missing_value_choice == '2':
    p = float(input("Enter momentum(p)"))
    v = float(input("Enter velocity(v)"))
    m = p / v
    print(f"mass(m) = {m}")
elif missing_value_choice == '1':
    m = float(input("Enter mass(m)"))
    v = float(input("Enter velocity(v)"))
    p = m * v
    print(f"momentum(p) = {p}")
else:
    print("invalid choice")
