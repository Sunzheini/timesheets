from db.database import months_to_numbers
from gui.front_end_settings import light_color_success, light_color_error
from support.excel_reader import read_from_excel_file, read_from_excel_file2
from support.support_functions import get_path_of_related_common_timesheets_file, get_path_of_related_project_file


class Engine:
    def __init__(self, db_controller):
        self.db_controller_object = db_controller

    @staticmethod
    def methods_bound_to_dropdown(request_info):
        return_result = 'Избрано: ' + ', '.join(request_info)
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message

    def methods_bound_to_button_1(self, request_info):
        # Split the request info ----------------------------------------------------------
        name = request_info[0]
        year = request_info[1]
        month = request_info[2]
        folder_path = request_info[3]
        list_of_projects_for_the_month = []

        # Get the path of the timesheets file ---------------------------------------------
        timesheets_file_path = get_path_of_related_common_timesheets_file(year, folder_path)
        if 'Error' in timesheets_file_path:
            return_result = timesheets_file_path
            status_color = light_color_error
            additional_message = None
            return return_result, status_color, additional_message

        # Read the data from the Common Timesheets file ------------------------------------
        try:
            return_result = read_from_excel_file(
                timesheets_file_path, name, year, month,
            )
        except Exception as e:
            return_result = 'Error: ' + str(e)
            status_color = light_color_error
            additional_message = None
            return return_result, status_color, additional_message

        # Fill-in the list of projects from the data ---------------------------------------
        for project in return_result:
            if 'Total' not in project:
                list_of_projects_for_the_month.append(project)

        # for each project in the list of projects -----------------------------------------
        for current_project in list_of_projects_for_the_month:

            # ToDo: temporary
            if current_project != '4BIZ':
                continue

            # Get the path to the project file ---------------------------------------------
            project_file_path = get_path_of_related_project_file(current_project, folder_path)

            # Read the data from the project file ------------------------------------------
            month_number = months_to_numbers[month]
            sheet_name = f'{month_number}.{year}'
            dict_to_compare = return_result[current_project]

            try:
                return_result2 = read_from_excel_file2(project_file_path, sheet_name, dict_to_compare)
            except Exception as e:
                return_result2 = 'Error: ' + str(e)
                status_color = light_color_error
                additional_message = None
                return return_result2, status_color, additional_message

        # Return the result ----------------------------------------------------------------
        status_color = light_color_success
        additional_message = None
        return return_result2, status_color, additional_message

    def methods_bound_to_button_2(self, request_info):
        return_result = self.db_controller_object.get_employee_names()
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message
