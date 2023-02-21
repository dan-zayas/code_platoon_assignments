from classes.school import School 

# def input_str_to_int(value):
#     try:
#         mode = int(input(prompt))
#     except ValueError:
#         print("Don't be a jabroni. Please enter a valid number.")
#         continue

school = School('School of Hard Knocks') 

prompt = '''
What do you want?
Options:
    1. List All Students
    2. View Individual Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
'''

while True:
    try:
        mode = int(input(prompt))
    except ValueError:
        print("Don't be a jabroni. Please enter a valid number.")
        continue

    if mode == 1:
        student_list = school.get_all_students()
        for student in student_list:
            print(student)

    elif mode == 2:
        try: 
            id = input("What's their id then?")
        except:
            print("That's not anyone here.")
        student = school.get_student_by_id(id)
        if student: print(student)

    elif mode == 3:
        new_student = {}
        new_student['name'] = input("Name: ")
        new_student['age'] = input("Age: ")
        new_student['role'] = "Student"
        new_student['password'] = input("Password: ")
        new_student['school_id'] = input("School ID: ")
        updated_student_list = school.add_student(new_student)

        print(updated_student_list)

    elif mode == 4:
        school.remove_student_by_id(324)
    elif mode == 5:
        break