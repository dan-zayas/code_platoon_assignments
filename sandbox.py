import math


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def work(self):
        print(f"{self.name} is working hard as a {self.job}.")


ben = Person("Ben", "teacher")
ben.work()

# just to break up the output a little
print()


class Computer:
    def __init__(self, number_of_cores):
        self.number_of_cores = number_of_cores

    def compute(self):
        pi = round(math.pi, self.number_of_cores)
        print(f"Computing pi to {self.number_of_cores} decimal places: {pi}")


toaster = Computer(1)
toaster.compute()

chappy = Computer(4)
chappy.compute()

print()


class Cyborg:
    # note the meaning of 'super()' is ambiguous when inheriting from multiple parents
    # so this is how you reference the specific (internal) parent object instead
    def __init__(self, name, job, number_of_cores):
        Person.__init__(self, name, job)
        Computer.__init__(self, number_of_cores)

    def work(self):
        print(f"{self.name} has the strength of {self.number_of_cores} men! Watch:")
        for n in range(self.number_of_cores):
            Person.work(self)
        print("And he is still a fully functioning computer!")
        Computer.compute(self)


terminator = Cyborg('Arnold', 'terminator', 8)
terminator.work()