from db.database import employees, years, months


class DatabaseController:
    """
    DatabaseController class is responsible for handling all the database operations. In the current
    implementation, the database comprises dictionaries.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_employee_names():
        """
        This method returns the list of employee names from the database.
        :return: list of employee names
        """
        employee_names_list = []
        for employee in employees.keys():
            employee_names_list.append(employees[employee]['name'])
        return employee_names_list

    @staticmethod
    def get_years():
        """
        This method returns the list of years from the database.
        :return: list of years
        """
        return years

    @staticmethod
    def get_months():
        """
        This method returns the list of months from the database.
        :return: list of months
        """
        return months
