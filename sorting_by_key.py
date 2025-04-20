# Sample list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20}
]

# Sorting the list of dictionaries by the 'age' key
sorted_people = sorted(people, key=lambda person: person["age"], reverse=True)
sorted_people2 = sorted(people, key=lambda person: person["age"], reverse=False)


for person in sorted_people:
    print(person)

for person in sorted_people2:
    print(person)
