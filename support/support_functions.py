import os


def get_list_of_all_files_in_a_folder(folder_path):
    """
    Get a list of all files in a folder
    :param folder_path: the path to the folder
    :return: a list of all files in the folder
    """
    files_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            files_list.append(file)
    return files_list


def get_path_of_related_common_timesheets_file(year, folder_path):
    """
    Get the path of the timesheets file for the given year
    :param year: the year to search for
    :param folder_path: the path to the folder
    :return: the path to the timesheets file for the given year
    """
    files_in_the_folder = get_list_of_all_files_in_a_folder(folder_path)

    # check file name for year
    for file in files_in_the_folder:
        if year in file:
            return os.path.join(folder_path, file)
    return 'Error: Could not find the timesheets file for the given year'


def get_path_of_related_project_file(project_name, folder_path):
    """
    Get the path of the project file for the given project name
    :param project_name: the name of the project
    :param folder_path: the path to the folder
    :return: the path to the project file for the given project name
    """
    files_in_the_folder = get_list_of_all_files_in_a_folder(folder_path)

    # check file name for project name
    for file in files_in_the_folder:
        if project_name.lower().strip() in file.lower() and '.xlsx' in file:
            return os.path.join(folder_path, file)
    return f'Error: Could not find the project file for the given project in Common: {project_name}'


def prettify_nested_dict(type_string, dict_to_prettify):
    """
    Prettify a nested dictionary
    :param type_string: the type of the dictionary, which is either 'common' or 'project'
    :param dict_to_prettify: the dictionary to prettify
    :return: the prettified dictionary for display
    """
    if type_string == 'common':
        return_string = '\n' + '--- Common Timesheets ---' + '\n'
    elif type_string == 'project':
        return_string = '\n' + '--- Timesheets по проекти ---' + '\n'

    for key in dict_to_prettify.keys():
        return_string += f'{key}:' + '\n'
        for inner_key in dict_to_prettify[key].keys():
            return_string += f'{inner_key}: {dict_to_prettify[key][inner_key]}, '
        return_string += '\n'

    return return_string


def add_a_total_dict_to_nested_dict(dict_to_add_total_to):
    """
    Add a total dictionary to a nested dictionary by summing up the values of the inner dictionaries
    :param dict_to_add_total_to: the dictionary to add the total dictionary to
    :return: the dictionary with the total dictionary added
    """
    total_dict_key = 'Total Ʃ Hours'
    total_dict_value = {}

    for key, value in dict_to_add_total_to.items():
        for inner_key, inner_value in value.items():
            if inner_key not in total_dict_value:
                total_dict_value[inner_key] = inner_value
            else:
                total_dict_value[inner_key] += inner_value

    dict_to_add_total_to[total_dict_key] = total_dict_value
    return dict_to_add_total_to


def evaluate_results(common_dict, project_dict):
    """
    Evaluate the results of the common and project dictionaries with respect to the total hours
    :param common_dict: the common dictionary
    :param project_dict: the project dictionary
    :return: the evaluation result
    """
    return_string = '\n' + '--- Оценка на общите часове ---' + '\n'

    common_dict_criteria = None
    for key in common_dict.keys():
        if 'Total' in key:
            common_dict_criteria = common_dict[key]

    project_dict_criteria = None
    for key in project_dict.keys():
        if 'Total' in key:
            project_dict_criteria = project_dict[key]

    if common_dict_criteria and project_dict_criteria:
        if common_dict_criteria == project_dict_criteria:
            return_string += 'Съвпадение'
        else:
            return_string += 'Наличие на разлики: '

            for key in common_dict_criteria.keys():
                if common_dict_criteria[key] != project_dict_criteria[key]:
                    # return_string += f'{key}: {common_dict_criteria[key]} != {project_dict_criteria[key]}, '
                    return_string += 'в Common: ' + f'{key}: {common_dict_criteria[key]}, '
                    return_string += 'в Project: ' + f'{key}: {project_dict_criteria[key]}, '

    return return_string
