"""
In the current implementation the database is hardcoded in the database.py file.
"""


class DataBase:
    def __init__(self):
        self.employees = {
            '----': 0,
        }
        self.actual_projects = []
        self.years = [
            2020,
            2021,
            2022,
            2023,
            2024,
        ]
        self.months = [
            'january',
            'february',
            'march',
            'april',
            'may',
            'june',
            'july',
            'august',
            'september',
            'october',
            'november',
            'december',
        ]
        self.months_to_numbers = {
            'january': 1,
            'february': 2,
            'march': 3,
            'april': 4,
            'may': 5,
            'june': 6,
            'july': 7,
            'august': 8,
            'september': 9,
            'october': 10,
            'november': 11,
            'december': 12,
        }


column_of_month_in_common_timesheets_file = 24
column_of_year_in_common_timesheets_file = 30

default_folder_path: str = r'C:\Users\User\Desktop\Marine Cluster BG\Files'
