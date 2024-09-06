"""
In the current implementation the database is hardcoded in the database.py file.
"""

employees = {
    1: {
        'name': 'Irina Kircheva',
        'position': 'Специалист по кадрови въпроси',
        'born_after_31.12.1959': True,
        'contact': False,
        'hourly_rate_in_leva': 20,
        'monthly_salary_in_leva': 0,
    },
    2: {
        'name': 'Genka Rafailova',
        'position': 'Специалист по кадрови въпроси',
        'born_after_31.12.1959': True,
        'contact': True,
        'hourly_rate_in_leva': 0,
        'monthly_salary_in_leva': 3000,
    },
    3: {
        'name': 'Daniela Chonkova',
        'position': 'Специалист по кадрови въпроси',
        'born_after_31.12.1959': False,
        'contact': False,
        'hourly_rate_in_leva': 22,
        'monthly_salary_in_leva': 0,
    },
    4: {
        'name': 'Maria Zlateva',
        'position': 'Специалист по кадрови въпроси',
        'born_after_31.12.1959': False,
        'contact': True,
        'hourly_rate_in_leva': 0,
        'monthly_salary_in_leva': 3200,
    },
}

years = [
    2020,
    2021,
    2022,
    2023,
    2024,
]

months = [
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

months_to_numbers = {
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
