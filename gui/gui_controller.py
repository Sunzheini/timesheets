import os
import time
from tkinter import filedialog
from tkinter import *
from tkinter import font
from tkinter import scrolledtext

from support.decorators import time_measurement_decorator
from gui.front_end_settings import (roboto_font_family, roboto_font_size,
                                    apply_the_front_end_settings, apply_the_browse_buttons,
                                    apply_the_browse_labels, apply_the_work_buttons,
                                    apply_light_next_to_work_buttons,
                                    name_of_browse_label1, name_of_browse_button1, name_of_button1,
                                    name_of_button2, name_of_button3, default_status_text,
                                    status_label_background_color, status_label_foreground_color, light_color_error,
                                    light_color_success, light_fill_color_neutral, data_section_height,
                                    data_section_start_y, label_background_color, config_the_dropdown_menu)


class MyGui:
    """
    This class is responsible for the GUI of the application.
    """
    DEFAULT_STATUS_TEXT = default_status_text
    FONT_FAMILY = roboto_font_family
    FONT_SIZE = roboto_font_size

    def __init__(
            self,
            engine_object,                                  # responsible for the logic of the application
    ):
        """
        This is the constructor of the class.
        Creates the window and all the elements inside it, see below.
        :param engine_object: responsible for the logic of the application
        """

        # -----------------------------------------------------------------------------
        # General window looks
        # -----------------------------------------------------------------------------
        self.window = Tk()
        self.window = apply_the_front_end_settings(self.window)
        app_font = font.Font(family=self.FONT_FAMILY, size=self.FONT_SIZE)

        # -----------------------------------------------------------------------------
        # External objects
        # -----------------------------------------------------------------------------
        self.engine_object = engine_object

        # -----------------------------------------------------------------------------
        # Internal objects
        # -----------------------------------------------------------------------------
        self.contents_of_status_label = self.DEFAULT_STATUS_TEXT
        self.selected_path = None

        # -----------------------------------------------------------------------------
        # Names of elements
        # -----------------------------------------------------------------------------
        self.name_of_browse_label1 = name_of_browse_label1
        self.name_of_browse_button1 = name_of_browse_button1
        self.name_of_button1 = name_of_button1
        self.name_of_button2 = name_of_button2
        self.name_of_button3 = name_of_button3

        # -----------------------------------------------------------------------------
        # Browse Buttons
        # -----------------------------------------------------------------------------
        self.browse_button_1 = apply_the_browse_buttons(self.window)
        self.browse_button_1.config(command=self.select_location)
        self.browse_button_1.place(x=10, y=10)

        # -----------------------------------------------------------------------------
        # Browse Labels
        # -----------------------------------------------------------------------------
        self.browse_label_1 = apply_the_browse_labels(self.window)
        self.browse_label_1.config(font=(self.FONT_FAMILY, self.FONT_SIZE, "italic"))
        self.browse_label_1.place(x=200, y=11)

        # -----------------------------------------------------------------------------
        # Create a line separator under the browse section
        # -----------------------------------------------------------------------------
        self.line_sep = Frame(self.window, height=2, bd=1, relief='sunken')
        self.line_sep.place(x=10, y=46, width=780, height=2)

        # -----------------------------------------------------------------------------
        # Data section
        # -----------------------------------------------------------------------------
        self.employee_names_options = self.engine_object.db_controller_object.get_employee_names()
        self.selected_option1 = StringVar()                         # Define a Tkinter var to store the selected option
        self.selected_option1.set(self.employee_names_options[0])   # Set the default value to the first option
        self.dropdown_menu1 = OptionMenu(self.window, self.selected_option1, *self.employee_names_options)
        self.dropdown_menu1 = config_the_dropdown_menu(self.dropdown_menu1, app_font)
        self.dropdown_menu1.place(x=10, y=data_section_start_y)

        self.years_options = self.engine_object.db_controller_object.get_years()
        self.selected_option2 = StringVar()
        current_year = time.localtime().tm_year
        self.selected_option2.set(str(current_year))
        self.dropdown_menu2 = OptionMenu(self.window, self.selected_option2, *self.years_options)
        self.dropdown_menu2 = config_the_dropdown_menu(self.dropdown_menu2, app_font)
        self.dropdown_menu2.place(x=200, y=data_section_start_y)

        self.months_options = self.engine_object.db_controller_object.get_months()
        self.selected_option3 = StringVar()
        current_month = time.localtime().tm_mon
        self.selected_option3.set(self.months_options[current_month-2])
        self.dropdown_menu3 = OptionMenu(self.window, self.selected_option3, *self.months_options)
        self.dropdown_menu3 = config_the_dropdown_menu(self.dropdown_menu3, app_font)
        self.dropdown_menu3.place(x=390, y=data_section_start_y)

        def execute_on_dropdown_select(*args):
            selected_option1 = self.selected_option1.get()
            selected_option2 = self.selected_option2.get()
            selected_option3 = self.selected_option3.get()
            self.commands_bound_to_dropdown_menu(selected_option1, selected_option2, selected_option3)

        # Bind the print_selected_option function to the selected_option variable
        self.selected_option1.trace("w", execute_on_dropdown_select)
        self.selected_option2.trace("w", execute_on_dropdown_select)
        self.selected_option3.trace("w", execute_on_dropdown_select)

        # -----------------------------------------------------------------------------
        # Create a line separator under the data section
        # -----------------------------------------------------------------------------
        # self.line_sep = Frame(self.window, height=2, bd=1, relief='sunken')
        # self.line_sep.place(x=10, y=data_section_height+140, width=780, height=2)

        # -----------------------------------------------------------------------------
        # Work Buttons
        # -----------------------------------------------------------------------------
        self.work_button_1, self.work_button_2, self.work_button_3 = (
            apply_the_work_buttons(self.window))

        self.work_button_1.config(command=self.commands_bound_to_work_button_1)
        self.work_button_2.config(command=self.commands_bound_to_work_button_2)
        self.work_button_3.config(command=self.commands_bound_to_work_button_3)

        self.work_button_1.place(x=10+570, y=data_section_start_y+1)
        # self.work_button_2.place(x=295, y=data_section_height+155)    # ToDo: until it is used
        self.work_button_3.place(x=580, y=data_section_height+155)

        # -----------------------------------------------------------------------------
        # Bind keyboard shortcuts to work buttons
        # -----------------------------------------------------------------------------
        self.window.bind_all('<a>', self.commands_bound_to_work_button_1)
        self.window.bind_all('<s>', self.commands_bound_to_work_button_2)
        self.window.bind_all('<d>', self.commands_bound_to_work_button_3)

        # -----------------------------------------------------------------------------
        # Lights next to work buttons
        # -----------------------------------------------------------------------------
        self.canvas1, self.canvas2, self.canvas3, self.rect1, self.rect2, self.rect3 = (
            apply_light_next_to_work_buttons(self.window))

        self.canvas1.place(x=195+570, y=data_section_start_y+1)
        # self.canvas2.place(x=480, y=data_section_height+155)
        self.canvas3.place(x=765, y=data_section_height+155)

        # -----------------------------------------------------------------------------
        # Create a line separator under the work buttons section
        # -----------------------------------------------------------------------------
        self.line_sep = Frame(self.window, height=2, bd=1, relief='sunken')
        self.line_sep.place(x=10, y=data_section_height+207, width=780, height=2)

        # -----------------------------------------------------------------------------
        # Status label
        # -----------------------------------------------------------------------------
        self.status_label = scrolledtext.ScrolledText(
            self.window,
            width=108,
            height=25,
            wrap=WORD,
            bg=status_label_background_color,
            fg=status_label_foreground_color,
            border=0,
            padx=5,
            pady=5,
            relief='solid',
            font=app_font,
        )
        self.status_label.place(x=10, y=data_section_height+222)
        self.status_label.insert(END, self.contents_of_status_label)

    # -----------------------------------------------------------------------------
    # Methods on browse buttons
    # -----------------------------------------------------------------------------
    @time_measurement_decorator
    def select_location(self, path=None):
        """
        Select the location of the project directory. If the path is not specified,
        a file dialog is opened. Otherwise, the specified path is used. Then the
        location is updated in the database and the label next to the browse button.
        :param path: the path to be used if specified
        :return: None
        """
        if path is None:
            filepath = filedialog.askdirectory()
        else:
            filepath = path

        self.selected_path = filepath
        self.update_label_next_to_browse_button(self.browse_label_1, f"{self.selected_path}")
        self.update_status_label(f"Избрано: '{self.selected_path}'")

    @staticmethod
    def update_label_next_to_browse_button(label_number, text):
        """
        Updates the label next to the browse button.
        :param label_number: the label to update
        :param text: the text to update the label with
        :return: None
        """
        label_number.config(text=text)
        label_number.config(anchor='w')

    # -----------------------------------------------------------------------------
    # Methods on dropdown menu
    # -----------------------------------------------------------------------------
    @time_measurement_decorator
    def commands_bound_to_dropdown_menu(self, selected_option1, selected_option2, selected_option3):
        """
        This method is bound to the dropdown menu and executes the functions bound to it.
        :param selected_option1: the selected employee name
        :param selected_option2: the selected year
        :param selected_option3: the selected month
        """
        # execute functions and get the result, color and additional message if any
        request_info = selected_option1, selected_option2, selected_option3
        try:
            return_result, status_color, additional_message = self.engine_object.methods_bound_to_dropdown(
                request_info)
        except Exception as e:
            return_result, status_color, additional_message = f"Грешка: '{e}'", light_color_error, None

        # if there is an additional message, show it
        if additional_message is not None:
            self.update_status_label(f"'{return_result}'\n{additional_message}")
        else:
            self.update_status_label(f"'{return_result}'")

    # -----------------------------------------------------------------------------
    # Methods on work buttons
    # -----------------------------------------------------------------------------
    @time_measurement_decorator
    def commands_bound_to_work_button_1(self, event=None):
        """
        This method is bound to the first work button and executes the functions
        bound to it. It also updates the light next to the button and the status label.
        :param event: not used
        :return: None
        """
        # execute functions and get the result, color and additional message if any
        request_info = (
            self.selected_option1.get(),
            self.selected_option2.get(),
            self.selected_option3.get(),
            self.selected_path,
        )
        try:
            return_result, status_color, additional_message = self.engine_object.methods_bound_to_button_1(request_info)
        except Exception as e:
            return_result, status_color, additional_message = f"Грешка: '{e}'", light_color_error, None

        # feedback to the light next to the button
        self.update_light_next_to_button(self.canvas1, self.rect1, status_color)

        # if there is an additional message, show it
        if additional_message is not None:
            self.update_status_label(f"'{return_result}'\n{additional_message}")
        else:
            self.update_status_label(f"'{return_result}'")

    @time_measurement_decorator
    def commands_bound_to_work_button_2(self, event=None):
        """
        This method is bound to the second work button and executes the functions
        bound to it. It also updates the light next to the button and the status label.
        :param event: not used
        :return: None
        """
        # execute functions and get the result, color and additional message if any
        request_info = None
        try:
            return_result, status_color, additional_message = self.engine_object.methods_bound_to_button_2(request_info)
        except Exception as e:
            return_result, status_color, additional_message = f"Грешка: '{e}'", light_color_error, None

        # feedback to the light next to the button
        self.update_light_next_to_button(self.canvas2, self.rect2, status_color)

        # if there is an additional message, show it
        if additional_message is not None:
            self.update_status_label(f"Операция 2: '{return_result}'\n{additional_message}")
        else:
            self.update_status_label(f"Операция 2: '{return_result}'")

    @time_measurement_decorator
    def commands_bound_to_work_button_3(self, event=None):
        """
        This method is bound to the third work button and clears the status label.
        :param event: not used
        :return: None
        """
        # clear the status label
        self.contents_of_status_label = self.DEFAULT_STATUS_TEXT
        self.status_label.delete('1.0', END)

        # set the light to green for 1 second
        self.update_light_next_to_button(self.canvas3, self.rect3, light_color_success)
        self.window.after(1000, self.update_light_next_to_button, self.canvas3, self.rect3, light_fill_color_neutral)

    @staticmethod
    def update_light_next_to_button(canvas_number, rect_number, color):
        """
        Updates the light next to the work button.
        :param canvas_number: the canvas to update
        :param rect_number: the rectangle to update
        :param color: the color to update the light with
        :return: None
        """
        canvas_number.itemconfig(rect_number, fill=color, outline=color)

    def update_status_label(self, text):
        """
        Updates the status label. If the label is empty, it clears it first. Otherwise,
        it adds the new text to the existing text. Then it clears the existing text and
        inserts the updated text.
        :param text: the text to update the label with
        :return: None
        """
        # if the status label is empty, clear it
        if self.contents_of_status_label == self.DEFAULT_STATUS_TEXT:
            self.contents_of_status_label = ''

        # add the new text to the existing text
        self.contents_of_status_label += text + '\n'

        # Clear the existing text and insert the updated text
        self.status_label.delete('1.0', END)
        self.status_label.insert(END, self.contents_of_status_label)

    # -----------------------------------------------------------------------------
    # Running the frontend
    # -----------------------------------------------------------------------------
    def run(self):
        """
        Runs the frontend.
        """
        self.window.mainloop()

    def on_exit(self):
        """
        This function is executed when the user closes the window. You can override it
        to perform any final operations or save data before the window is closed.
        Currently, it closes the database connection and quits the window.
        """
        self.window.quit()
