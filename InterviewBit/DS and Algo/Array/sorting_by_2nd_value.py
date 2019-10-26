# Sort based on 2nd value
students = [['G', 10], ['A', 22], ['S', 1], ['P', 14]]
print(sorted(students, key=lambda student: student[1]))

print(sorted("This is a test string from Andrew".split(), key=str.lower))  