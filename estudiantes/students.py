
class Student:
    name: str
    edad: str
    notas: list[int]

    def __init__(self, name, edad, notas):
        self.name = name,
        self.edad = edad,
        self.notas = notas

    @staticmethod
    def get_promedio(student):
        return lambda x: sum(x)/len(x), student.notas


class StudentSet:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def is_aproved(self, student):
        if student.get_promedio() >= 6:
            return True
        return False

    def list_approved(self):
        return filter(self.is_aproved(), self.students)
    
    def list_failed(self):
        return filter(not (self.is_aproved()), self.students)
    

Juan = Student("Tomi", "25", ["10", "5", "4"])

promedio, list = Juan.get_promedio(Juan)


print(promedio(list))