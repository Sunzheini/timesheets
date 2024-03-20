from gui.front_end_settings import light_color_success


class Engine:
    def __init__(self, db_controller):
        self.db_controller_object = db_controller

    def methods_bound_to_dropdown(self, request_info):
        return_result = request_info
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message

    def methods_bound_to_button_1(self, request_info):
        return_result = self.db_controller_object.get_employee_names()
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message

    def methods_bound_to_button_2(self, request_info):
        return_result = self.db_controller_object.get_employee_names()
        status_color = light_color_success
        additional_message = None
        return return_result, status_color, additional_message
