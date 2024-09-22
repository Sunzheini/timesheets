from support.excel_reader import get_employee_names_and_hourly_rate_from_the_excel_database


class DatabaseController:
    """
    DatabaseController class is responsible for handling all the database operations. In the current
    implementation, the database comprises dictionaries.
    """
    def __init__(self, database):
        self.database = database

    def update_database(self, path_to_file):
        employee_data = get_employee_names_and_hourly_rate_from_the_excel_database(path_to_file)
        self.database.employees = employee_data


    def get_employee_names(self):
        """
        This method returns the list of employee names from the database.
        :return: list of employee names
        """
        employee_names_list = []
        for employee in self.database.employees.keys():
            employee_names_list.append(employee)
        return employee_names_list

    def get_months_to_numbers(self):
        """
        This method returns the dictionary of months to numbers from the database.
        :return: dictionary of months to numbers
        """
        return self.database.months_to_numbers

    def get_months(self):
        """
        This method returns the list of months from the database.
        :return: list of months
        """
        return self.database.months

    def get_years(self):
        """
        This method returns the list of years from the database.
        :return: list of years
        """
        return self.database.years

    def get_months(self):
        """
        This method returns the list of months from the database.
        :return: list of months
        """
        return self.database.months
