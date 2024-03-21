import os


def get_list_of_all_files_in_a_folder(folder_path):
    files_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            files_list.append(file)
    return files_list


def get_path_of_related_common_timesheets_file(year, folder_path):
    files_in_the_folder = get_list_of_all_files_in_a_folder(folder_path)

    # check file name for year
    for file in files_in_the_folder:
        if year in file:
            return os.path.join(folder_path, file)
    return 'Error: Could not find the timesheets file for the given year'

