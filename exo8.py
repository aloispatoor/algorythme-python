class Student:
    name = ""
    surname = ""
    note = []

    def __init__(self, name : str, surname : str, note : int):
        self.name = name
        self.surname = surname
        self.note = note

    def studentAverage(self, note :list[int]) -> int:
        i = len(self.note)
        sum = 0
        for i in note:
            sum = sum + i
        average = sum / i
        return average

class Classe:
    listStudent = []

    def __init__(self) -> None:
        pass
    
    def addStudent(self, student : Student):
        self.listStudent.append(student)

    def classeAverage(self, studentsAverage : list[int]) -> int:
        i = len(self.listStudent)
        sum = 0
        for i in studentsAverage:
            sum = sum + i
        average = sum / i
        return average

Robert = Student("Gobaert", "Robert", [9, 15, 17, 13, 12, 8])
Theo = Student("Ravi", "Théo", [7, 8, 17, 16, 4, 11])

averageRobert = Student.studentAverage(Robert)
averageTheo = Student.studentAverage(Theo)
print(f"La moyenne de {Robert.surname} est de {averageRobert}")
print(f"La moyenne de {Theo.surname} est de {averageTheo}")


    