people = [
    {"name":"Harry", "House": "Gryffindor"},
    {"name": "Cho", "House": "Ravenclaw"},
    {"name": "Draco:", "House": "Stytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)