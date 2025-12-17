Time = 3
array_e = []
array_c = []

for i in range(Time):
    try:
        a = int(input("Enter person (entering): "))
        array_e.append(a)
        b = int(input("Enter person (going): "))
        array_c.append(b)
        print("array_e: ", array_e)
        print("array_c: ", array_c)
    except ValueError:
        print("Error: Please enter a valid integer.")
        break
array_b = [e - c for c, e in zip(array_c, array_e)]
print("array_b:", array_b)
t = sum(array_b)
print("Left Person:", t)