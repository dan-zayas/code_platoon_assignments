from .person import Person
from csv import DictReader

class Student(Person):
    def __init__(self, **kwargs):
        super().__init__(kwargs['name'], kwargs['age'], kwargs['role'], kwargs['password'])
        self.school_id = int(kwargs['school_id'])

    @classmethod
    def load_students_from_csv(student_cls):
        student_list = []
        with open("./data/students.csv") as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                new_student = student_cls(**row)
                student_list.append(new_student)

        return student_list
    
    def __str__(self):
        return f"Name: {self.name} -- age: {self.age} -- id {self.school_id}"
