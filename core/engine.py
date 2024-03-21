from gui.front_end_settings import light_color_success, light_color_error
from support.excel_reader import read_from_excel_file
from support.support_functions import get_path_of_related_common_timesheets_file


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

        # Get the path of the timesheets file ---------------------------------------------
        timesheets_file_path = get_path_of_related_common_timesheets_file(year, folder_path)
        if 'Error' in timesheets_file_path:
            return_result = timesheets_file_path
            status_color = light_color_error
            additional_message = None
            return return_result, status_color, additional_message

        # Read the data from the Excel file ----------------------------------------------
        try:
            return_result = read_from_excel_file(timesheets_file_path, name, year, month)
        except Exception as e:
            return_result = 'Error: ' + str(e)
            status_color = light_color_error
            additional_message = None
            return return_result, status_color, additional_message

        # Return the result ----------------------------------------------------------------
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message

    def methods_bound_to_button_2(self, request_info):
        return_result = self.db_controller_object.get_employee_names()
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message
