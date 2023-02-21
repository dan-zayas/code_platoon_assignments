from .person import Person
from csv import DictReader

class Staff(Person):
    def __init__(self, **kwargs):
        super().__init__(kwargs['name'], kwargs['age'], kwargs['role'], kwargs['password'])
        self.employee_id = int(kwargs['employee_id'])

    @classmethod
    def load_staff_from_csv(staff_cls):

        staff_list = []
        with open("./data/staff.csv") as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                new_staff = staff_cls(**row)
                staff_list.append(new_staff)
    
        return staff_list