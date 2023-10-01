class Student:
    def __init__(self, name, currentClass, id):
        self.name = name
        self.id = id
        self.currentClass = currentClass

    def __repr__(self) -> str:
        return f'Student with name {self.name}, class: {self.currentClass}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def addTeacher(self, teacherName, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(teacherName, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee-6500}'

    def __repr__(self) -> str:
        print("Welcome to", self.name)
        print("----Out Teachers----")
        for teacher in self.teachers:
            print(teacher)
        print("----Out Students----")
        for student in self.teachers:
            print(student)
        return 'All done for now'


alia = Student('alia torkari', 9, 1)
print(alia)

ranbeer = Teacher('Douran beer', 'algorithm', 101)
print(ranbeer)

phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('bani', 7000)
phitron.enroll('dani', 90000)

phitron.addTeacher('Jhankar', 'DS')
phitron.addTeacher('mahbub', 'algo')
phitron.addTeacher('sir', 'database')

print(phitron)
