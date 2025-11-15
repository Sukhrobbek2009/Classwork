class school:
    def __init__(self, student):
        self.student = student

    def add_student(self, name):
        self.student.append(name)

    def show_student(self):
        for student in self.student:
            print(student)

student = school(["Sam", "Rob"])