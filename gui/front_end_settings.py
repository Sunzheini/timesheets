from tkinter import Button, Label, Canvas


# data section settings ----------------------------------------------------------------------
data_section_height = 100
data_section_start_y = 60


# general -----------------------------------------------------------------------------
app_name = 'timesheets'
app_version = 'v0.1a'
window_width = 800
window_height = 407 + data_section_height
roboto_font_family = 'Roboto'
roboto_font_size = 9
# window_background_color = '#E5E5E5'
window_background_color = '#7E969C'
default_status_text = 'Статус: готов'


# button names -------------------------------------------------------------------------
name_of_browse_label1 = 'Път към проекта: няма'
name_of_browse_button1 = 'Избери пътя към проекта'
name_of_button1 = 'Зареди <A>'
name_of_button2 = 'Сравни <S>'
name_of_button3 = 'Изчисти <D>'


# button settings ----------------------------------------------------------------------
browse_button_width = 25
browse_button_height = 1
shortcut_button_width = 5
shortcut_button_height = 1
shortcut_button_relief = 'flat'
shortcut_button_cursor = 'hand2'
work_button_width = 25
work_button_height = 1


# label settings -----------------------------------------------------------------------
browse_label_width = 84
browse_label_height = 1
label_relief = 'ridge'
# label_background_color = '#E5E5E5'
label_background_color = '#7E969C'
label_foreground_color = 'black'
status_label_background_color = '#FAFAFA'
status_label_foreground_color = '#444444'


# lights settings ----------------------------------------------------------------------
light_width = 15
light_height = 25
# light_background_color = '#E5E5E5'
light_background_color = '#7E969C'
light_fill_color_neutral = 'dark gray'
light_outline_color_neutral = 'dark gray'
light_color_success = 'green'
light_color_error = '#8B0000'


def apply_the_front_end_settings(window):
    """
    Applies the front end settings to the window
    :param window: to apply the settings to
    :return: the window with the applied settings
    """
    window.title(app_name + ', ' + app_version)
    window.eval("tk::PlaceWindow . center")
    x = window.winfo_screenwidth() * 3 // 10
    y = int(window.winfo_screenheight() * 0.2)
    window.geometry(f'{str(window_width)}x{str(window_height)}+' + str(x) + '+' + str(y))
    window.iconbitmap('static\\icon.ico')
    window.config(background=window_background_color)

    return window


def apply_the_browse_labels(window):
    """
    Applies the browse labels to the window
    :param window: to apply the labels to
    :return: the labels applied to the window
    """
    browse_label_1 = Label(
        window,
        text=name_of_browse_label1,
        width=browse_label_width,
        height=browse_label_height,
        bg=label_background_color,
        borderwidth=0,
        relief=label_relief,
        fg=label_foreground_color,
        pady=4,
        anchor='w',
    )

    return browse_label_1


def apply_the_browse_buttons(window):
    """
    Applies the browse buttons to the window
    :param window: to apply the buttons to
    :return: the buttons applied to the window
    """
    browse_button_1 = Button(
        window,
        text=name_of_browse_button1,
        width=browse_button_width,
        height=browse_button_height,
    )

    return browse_button_1


def config_the_dropdown_menu(dropdown_menu, app_font):
    dropdown_menu.config(
        width=20,
        font=app_font,
        bg=label_background_color,
        fg='white',
        relief='solid',
        cursor='hand2',
        borderwidth=1,
        highlightthickness=1,
    )
    return dropdown_menu


def apply_the_work_buttons(window):
    """
    Applies the work buttons to the window
    :param window: to apply the buttons to
    :return: the buttons applied to the window
    """
    work_button1 = Button(
        window,
        text=name_of_button1,
        width=work_button_width,
        height=work_button_height,
    )

    work_button2 = Button(
        window,
        text=name_of_button2,
        width=work_button_width,
        height=work_button_height,
    )

    work_button3 = Button(
        window,
        text=name_of_button3,
        width=work_button_width,
        height=work_button_height,
    )

    return work_button1, work_button2, work_button3


def apply_light_next_to_work_buttons(window):
    """
    Applies the lights next to the work buttons and creates the rectangles inside them
    :param window: to apply the lights to
    :return: the lights applied to the window and the rectangles inside them
    """
    light1 = Canvas(
        window,
        width=light_width,
        height=light_height,
        bd=0,
        highlightthickness=0,
        bg=light_background_color,
    )

    light2 = Canvas(
        window,
        width=light_width,
        height=light_height,
        bd=0,
        highlightthickness=0,
        bg=light_background_color,
    )

    light3 = Canvas(
        window,
        width=light_width,
        height=light_height,
        bd=0,
        highlightthickness=0,
        bg=light_background_color,
    )

    rect1 = light1.create_rectangle(
        2, 1, 10, 39,
        fill=light_fill_color_neutral,
        outline=light_outline_color_neutral,
    )

    rect2 = light2.create_rectangle(
        2, 1, 10, 39,
        fill=light_fill_color_neutral,
        outline=light_outline_color_neutral,
    )

    rect3 = light3.create_rectangle(
        2, 1, 10, 39,
        fill=light_fill_color_neutral,
        outline=light_outline_color_neutral,
    )

    return light1, light2, light3, rect1, rect2, rect3
