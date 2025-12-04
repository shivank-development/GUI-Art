import random
subject=[
    "shahrukh khan ",
    "virat kohli ",
    "A mumbai cat "
]


action=[
    "launches ",
    "cancels ",
    "orders "
]

places_of_thing=[
    "at red fort ",
    "at india gate ",
    "at ganaga gate "
]

while True:
    subjects = random.choice(subject)
    actions = random.choice(action)
    places_of_things=random.choice(places_of_thing)

    headline=f"BREAKING NEWS : {subjects}{actions}{places_of_things}"
    print("\n"+headline)
    user_input=input("\n Do you want another headline? (yes/No) : ").strip()
    if user_input=="no":
        break
print("\n Thanks for using the fake news hesdline generater. Have a fun day")    