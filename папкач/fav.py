class Pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

best_pupils = []
with open('pupil.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        data = line.split(' ')
        p = Pupil(data[0], data[1], int(data[2]))
        if p.mark == 5:
            best_pupils.append(p.surname)

print(best_pupils)