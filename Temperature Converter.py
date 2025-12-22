temp = float(input("Enter temperature: "))
unit = input("Unit (C/F): ").upper()

if unit == "C":
    print(f"{temp}°C → {(temp * 9/5) + 32:.2f}°F")

elif unit == "F":
    print(f"{temp}°F → {(temp - 32) * 5/9:.2f}°C")

else:
    print("❌ Invalid unit")
