students = [
    {"name": "heermione","house": "Gryfinder","patronus": "Otter"},
    {"name": "Harry","house": "Gryfinder","patronus": "Otter"},
    {"name": "Ron", "house": "Gryfinder","patronus": None},

]

for students in students:
    print(students["name"], students["house"], students["patronus"], sep="\n")