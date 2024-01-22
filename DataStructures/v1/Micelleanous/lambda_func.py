operations = {
    "average" : lambda seq : sum(seq) / len(seq),
    "total"   : sum,
    "top"     : max
}

students = [
    {"name" : "Rolf", "grades" : (96, 90, 95, 100)},
    {"name" : "Bob", "grades" : (56, 78, 80, 90)},
    {"name" : "Jen", "grades" : (98, 90, 95, 99)},
    {"name" : "Annie", "grades" : (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student : {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    result = operations[operation](grades)
    print(result)


