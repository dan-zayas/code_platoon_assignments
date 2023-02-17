from .staff import Staff
from .student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_staff_from_csv()
        self.students = Student.load_students_from_csv()


    def get_all_students(self):
        return self.students

    def get_student_by_id(self, id):
        for student in self.students:
            if student.school_id == id:
                return student
            
        print("Your kid doesn't go here.")
        return
    
    def add_student(self, new_student):
        self.students.append(Student(**new_student))
        return self.students
    
    def remove_student_by_id(self):
        return