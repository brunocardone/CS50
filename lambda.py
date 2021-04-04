people = [
    {"name": "João", "house": "Vila Olímpa"},
    {"name": "Joaquina", "house": "Vila Gumercindo"},
    {"name": "Rafael", "house": "Vila Mariana"}
]

def f(person):
    return person["name"]

#people.sort(key=f)

people.sort(key= lambda person: person["name"])

print(people)