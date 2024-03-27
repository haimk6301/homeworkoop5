from homeworkoop5.model.Person import Person


class Employee(Person):
    def __init__(self, name, age, company_name, salary):
        super().__init__(name, age)
        self.company_name = company_name
        self.salary = salary

    def print_employee(self):
        super().print_person()
        print(f'Works at: {self.company_name}, salary: {self.salary}')



