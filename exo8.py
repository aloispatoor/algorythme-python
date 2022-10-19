class Student:

    def __init__(self, name : str, surname : str, note : list[int]):
        self.name = name
        self.surname = surname
        self.note = note

    def studentAverage(self) -> int:
        i = len(self.note)
        return sum(self.note)/i

class Classe:

    def __init__(self, name : str, listStudent : list[Student]):
        self.name = name
        self.listStudent = listStudent

    def classeAverage(self) -> int:
        sum = 0
        for i in self.listStudent:
            sum = sum + i.studentAverage()
        return sum / len(self.listStudent)


Robert = Student("Gobaert", "Robert", [9, 15, 17, 13, 12, 8])
Theo = Student("Ravi", "Théo", [7, 8, 17, 16, 4, 11])

cm1 = Classe("CM1", [Robert, Theo])

averageRobert = Robert.studentAverage()
print(f"La moyenne de {Robert.surname} est de {averageRobert}")

averageTheo = Theo.studentAverage()
print(f"La moyenne de {Theo.surname} est de {averageTheo}")

averageCm1 = cm1.classeAverage()
print(f"La moyenne de la classe {cm1.name} est de {averageCm1}")


    