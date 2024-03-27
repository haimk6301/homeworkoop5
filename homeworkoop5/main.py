from homeworkoop5.model.Employee import Employee
from homeworkoop5.model.Person import Person

if __name__ == '__main__':
    person = Person('haim', 61)

    person.print_person()

    employee_1 = Employee('Avi', 38,'Microsoft', 30000)

    employee_1.print_employee()
