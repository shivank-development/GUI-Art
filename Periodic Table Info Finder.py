import periodictable as pt

name = input("Enter element name: ").capitalize()

# Get element by name (e.g. Hydrogen, Carbon, Gold)
element = getattr(pt, name, None)

if element:
    print("Name:", element.name)
    print("Symbol:", element.symbol)
    print("Atomic Number:", element.number)
    print("Atomic Weight:", element.mass)
    print("Density:", element.density)
else:
    print("Element not found!")
