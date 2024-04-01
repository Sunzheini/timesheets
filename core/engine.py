from db.database import months_to_numbers
from gui.front_end_settings import light_color_success, light_color_error
from support.excel_reader import read_from_excel_file_of_type_common, read_from_excel_file2
from support.support_functions import get_path_of_related_common_timesheets_file, get_path_of_related_project_file, \
    prettify_nested_dict, add_a_total_dict_to_nested_dict, evaluate_results


class Engine:
    """
    The Engine class is the main class that contains the methods that are bound to the buttons and dropdowns
    """
    def __init__(self, db_controller):
        self.db_controller_object = db_controller

    @staticmethod
    def methods_bound_to_dropdown(request_info):
        """
        This method is bound to the dropdown and is used to display the selected items
        :param request_info: the selected items
        :return: the selected items as a string, the color of the status, and an additional message
        """
        return_result = 'Избрано: ' + ', '.join(request_info)
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message

    @staticmethod
    def methods_bound_to_button_1(request_info):
        """
        This method is bound to the first button and is used to display the information
        gathered from the Common Timesheets and the project files for the selected month
        :param request_info: the selected items
        :return: the gathered information as a string, the color of the status, and an additional message
        """
        # 1. Split the request info ----------------------------------------------------------
        name = request_info[0]
        year = request_info[1]
        month = request_info[2]
        folder_path = request_info[3]
        list_of_projects_for_the_month = []
        return_result2 = {}

        # 2. Get the path of the timesheets file ---------------------------------------------
        try:
            timesheets_file_path = get_path_of_related_common_timesheets_file(year, folder_path)
        except Exception as e:
            timesheets_file_path = 'Error: folder path is not valid'

        if 'Error' in timesheets_file_path:
            return_result = timesheets_file_path
            status_color = light_color_error
            additional_message = None
            return return_result, status_color, additional_message

        # 3. Read the data from the Common Timesheets file ------------------------------------
        try:
            return_result = read_from_excel_file_of_type_common(
                timesheets_file_path, name, year, month,
            )
        except Exception as e:
            return_result = 'Error: ' + str(e)
            status_color = light_color_error
            additional_message = None
            return return_result, status_color, additional_message

        # 4. Fill-in the list of projects from the data ---------------------------------------
        for project in return_result:
            if 'Total' not in project:
                list_of_projects_for_the_month.append(project)

        # ----------------------------------------------------------------------------------
        # Phase 2
        # ----------------------------------------------------------------------------------

        # 5. for each project in the list of projects -----------------------------------------
        for current_project in list_of_projects_for_the_month:

            # 5.1. Get the path to the project file ---------------------------------------------
            project_file_path = get_path_of_related_project_file(current_project, folder_path)
            if 'Error' in project_file_path:
                return_result2 = project_file_path
                status_color = light_color_error
                additional_message = None
                return return_result2, status_color, additional_message

                # ToDo: 1. change ENN project name
                # ToDo: instead of reading the data, 2. insert a new column and 3. color the cells

            # 5.2. Read the data from the project file ------------------------------------------
            month_number = months_to_numbers[month]
            sheet_name = f'{month_number}.{year}'

            try:
                temp_project_dict_result = read_from_excel_file2(project_file_path, sheet_name)
                return_result2[current_project] = temp_project_dict_result
            except Exception as e:
                return_result2 = 'Error: ' + str(e)
                status_color = light_color_error
                additional_message = None
                return return_result2, status_color, additional_message

        # 6. Return the result ----------------------------------------------------------------
        string_to_return = (
            prettify_nested_dict('common', return_result)
            + prettify_nested_dict('project', add_a_total_dict_to_nested_dict(return_result2))
            + evaluate_results(return_result, return_result2)
        )

        status_color = light_color_success
        additional_message = None
        return string_to_return, status_color, additional_message

    def methods_bound_to_button_2(self, request_info):
        """
        This method is bound to the second button and is currently not used
        :param request_info: the selected items
        :return: the gathered information as a string, the color of the status, and an additional message
        """
        return_result = self.db_controller_object.get_employee_names()
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message
