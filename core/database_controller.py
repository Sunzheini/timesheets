from db.database import employees, years, months


class DatabaseController:
    def __init__(self):
        pass

    def get_employee_names(self):
        employee_names_list = []
        for employee in employees.keys():
            employee_names_list.append(employees[employee]['name'])
        return employee_names_list

    def get_years(self):
        return years

    def get_months(self):
        return months
