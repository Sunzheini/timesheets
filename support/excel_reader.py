from openpyxl import load_workbook
from db.database import column_of_month_in_common_timesheets_file, column_of_year_in_common_timesheets_file, months


def _determine_start_row_by_given_string(worksheet, month, year):
    int_year = int(year)
    capitalized_month = month.capitalize()
    for row in worksheet.iter_rows(min_row=1, max_row=worksheet.max_row,
                                   min_col=column_of_month_in_common_timesheets_file,
                                   max_col=column_of_month_in_common_timesheets_file):
        for cell in row:
            cell_value = cell.value
            if cell_value is None:
                continue

            if type(cell_value) == int:
                continue

            cell_value = cell_value.strip()
            if cell_value != capitalized_month:
                continue
            # check value of the cell in the same row but in column of year
            year_cell = worksheet[cell.row][column_of_year_in_common_timesheets_file].value
            if year_cell != int_year:
                continue
            return cell.coordinate


def get_the_info_related_to_the_employee(workbook, worksheet, coordinates):
    """
    '{'ScienceDiver': {
    	1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
    	16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 'Ʃ': '=SUM(C405:AG405)'},
      '4BIZ': {
    	1: 2, 2: 4, 3: 0, 4: 0, 5: 2, 6: 6, 7: 2, 8: 4, 9: 3, 10: 0, 11: 0, 12: 4, 13: 2, 14: 4, 15: 2,
    	16: 3, 17: 0, 18: 0, 19: 2, 20: 4, 21: 4, 22: 0, 23: 0, 24: 0, 25: 0, 26: 4, 27: 4, 28: 8, 29: 4, 30: 5, 31: 0, 'Ʃ': '=SUM(C406:AG406)'},
      'Bridge': {
    	1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
    	16: 1, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 1, 31: 0, 'Ʃ': '=SUM(C407:AG407)'},
      'InnoForward': {
    	1: 6, 2: 4, 3: 0, 4: 0, 5: 6, 6: 2, 7: 6, 8: 4, 9: 4, 10: 0, 11: 0, 12: 4, 13: 6, 14: 4, 15: 6,
    	16: 4, 17: 0, 18: 0, 19: 6, 20: 4, 21: 4, 22: 8, 23: 8, 24: 0, 25: 0, 26: 4, 27: 4, 28: 0, 29: 4, 30: 2, 31: 0, 'Ʃ': '=SUM(C408:AG408)'},
      'Total Ʃ Hours ': {
    	1: '=SUM(C405:C408)', 2: '=SUM(D405:D408)', 3: '=SUM(E405:E408)', 4: '=SUM(F405:F408)', 5: '=SUM(G405:G408)', 6: '=SUM(H405:H408)', 7: '=SUM(I405:I408)',
    	8: '=SUM(J405:J408)', 9: '=SUM(K405:K408)', 10: '=SUM(L405:L408)', 11: '=SUM(M405:M408)', 12: '=SUM(N405:N408)', 13: '=SUM(O405:O408)', 14: '=SUM(P405:P408)',
    	15: '=SUM(Q405:Q408)', 16: '=SUM(R405:R408)', 17: '=SUM(S405:S408)', 18: '=SUM(T405:T408)', 19: '=SUM(U405:U408)', 20: '=SUM(V405:V408)', 21: '=SUM(W405:W408)',
    	22: '=SUM(X405:X408)', 23: '=SUM(Y405:Y408)', 24: '=SUM(Z405:Z408)', 25: '=SUM(AA405:AA408)', 26: '=SUM(AB405:AB408)', 27: '=SUM(AC405:AC408)', 28: '=SUM(AD405:AD408)',
    	29: '=SUM(AE405:AE408)', 30: '=SUM(AF405:AF408)', 31: '=SUM(AG405:AG408)', 'Ʃ': '=SUM(AH405:AH408)'
       }
    }'
    """
    result = {}

    to_exit = False
    reference_cell_coordinate = None
    reference_cell_row = None
    reference_cell_column = None
    days_cell_coordinate = None
    days_cell_row = None
    days_cell_column = None

    for row in worksheet.iter_rows(min_row=worksheet[coordinates].row + 1, max_row=worksheet.max_row,
                                   min_col=1, max_col=1):

        if to_exit:
            break

        for cell in row:
            cell_value = cell.value
            if cell_value is None:
                continue

            if type(cell_value) == int:
                continue

            if 'Reference' not in cell_value:
                continue

            else:
                reference_cell_coordinate = cell.coordinate  # A404
                reference_cell_row = cell.row  # 404
                reference_cell_column = cell.column  # 1

                days_cell_coordinate = (
                    worksheet.cell(row=reference_cell_row - 1, column=reference_cell_column + 1).coordinate)  # B403
                days_cell_row = reference_cell_row - 1  # 403
                days_cell_column = reference_cell_column + 1  # 2

                # Fill the result dictionary -----------------------------------------------------
                break_on_next_iter = False
                counter = 1
                while 1:
                    if break_on_next_iter:
                        break

                    current_a_column_cell = worksheet.cell(
                        row=reference_cell_row + counter, column=reference_cell_column)

                    # check if contents of reference cell include 'Total' -------------------------
                    current_a_column_cell_contents = current_a_column_cell.value
                    if 'Total' in current_a_column_cell_contents:
                        break_on_next_iter = True

                    result[current_a_column_cell.value] = {}  # current_a_column_cell.value == 'ScienceDiver'

                    # for each row before empty cell in the same column ---------------------------
                    inner_counter = 1
                    while 1:

                        current_day_cell = worksheet.cell(
                            row=days_cell_row, column=days_cell_column + inner_counter)
                        if current_day_cell.value is None:
                            break

                        current_project_cell = worksheet.cell(
                            row=reference_cell_row + counter, column=reference_cell_column + 1 + inner_counter)

                        current_project_cell_value = current_project_cell.value
                        if current_project_cell_value is None:
                            current_project_cell_value = 0

                        result[current_a_column_cell.value][current_day_cell.value] = current_project_cell_value
                        inner_counter += 1

                    counter += 1

                to_exit = True
                break

    return result


def recalculate_because_of_formulas(time_dict):
    """
'{'ScienceDiver': {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0,
    14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
    26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 'Ʃ': 0},
  '4BIZ': {
    1: 2, 2: 4, 3: 0, 4: 0, 5: 2, 6: 6, 7: 2, 8: 4, 9: 3, 10: 0, 11: 0, 12: 4, 13: 2,
    14: 4, 15: 2, 16: 3, 17: 0, 18: 0, 19: 2, 20: 4, 21: 4, 22: 0, 23: 0, 24: 0, 25: 0,
    26: 4, 27: 4, 28: 8, 29: 4, 30: 5, 31: 0, 'Ʃ': 73},
  'Bridge': {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0,
    14: 0, 15: 0, 16: 1, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
    26: 0, 27: 0, 28: 0, 29: 0, 30: 1, 31: 0, 'Ʃ': 3},
  'InnoForward': {
    1: 6, 2: 4, 3: 0, 4: 0, 5: 6, 6: 2, 7: 6, 8: 4, 9: 4, 10: 0, 11: 0, 12: 4, 13: 6, 14: 4,
    15: 6, 16: 4, 17: 0, 18: 0, 19: 6, 20: 4, 21: 4, 22: 8, 23: 8, 24: 0, 25: 0, 26: 4, 27: 4,
    28: 0, 29: 4, 30: 2, 31: 0, 'Ʃ': 100},
  'Total Ʃ Hours ': {
    1: 8, 2: 8, 3: 0, 4: 0, 5: 8, 6: 8, 7: 8, 8: 8, 9: 8, 10: 0, 11: 0, 12: 8, 13: 8,
    14: 8, 15: 8, 16: 8, 17: 0, 18: 0, 19: 8, 20: 8, 21: 8, 22: 8, 23: 8, 24: 0, 25: 0,
    26: 8, 27: 8, 28: 8, 29: 8, 30: 8, 31: 0, 'Ʃ': 176
  }
}'
    """
    break_on_next_iter = False

    for project_key, value_dict in time_dict.items():
        if break_on_next_iter:
            break

        if 'Total' in project_key:
            sum_key = list(value_dict.keys())[-1]
            for day, hours in value_dict.items():
                if day == sum_key:
                    break_on_next_iter = True
                    continue

                value_dict[day] = 0
                for key, value in time_dict.items():
                    if 'Total' in key:
                        continue

                    value_dict[day] += int(value[day])

        # last item in value_dict is the sum key
        sum_key = list(value_dict.keys())[-1]
        total_sum = 0
        for day, hours in value_dict.items():
            if day == sum_key:
                continue

            total_sum += int(hours)

        time_dict[project_key][sum_key] = total_sum

    return time_dict


def read_from_excel_file(file_path, name, year, month):
    workbook = load_workbook(file_path)
    worksheet = workbook[name]
    coordinates = _determine_start_row_by_given_string(worksheet, month, year)  # X481
    # result = worksheet[coordinates].value                                            # September
    result = get_the_info_related_to_the_employee(workbook, worksheet, coordinates)
    result = recalculate_because_of_formulas(result)
    return result


def read_from_excel_file2(file_path, sheet_name, dict_to_compare):
    """
    :param file_path:
    :param sheet_name:
    :param dict_to_compare:
    {
        1: 2, 2: 4, 3: 0, 4: 0, 5: 2, 6: 6, 7: 2, 8: 4, 9: 3, 10: 0, 11: 0, 12: 4, 13: 2,
        14: 4, 15: 2, 16: 3, 17: 0, 18: 0, 19: 2, 20: 4, 21: 4, 22: 0, 23: 0, 24: 0, 25: 0,
        26: 4, 27: 4, 28: 8, 29: 4, 30: 5, 31: 0, 'Ʃ': 73
    }
    :return:
    """
    if len(sheet_name) == 6:
        sheet_name = '0' + sheet_name

    workbook = load_workbook(file_path)
    worksheet = workbook[sheet_name]

    # --------------------------------------------------------------------------------------------
    result = {}

    to_exit = False
    total_cell_coordinate = None
    total_cell_row = None
    total_cell_column = None
    days_cell_coordinate = None
    days_cell_row = None
    days_cell_column = None

    # ToDo: Debug from here
    for row in worksheet.iter_rows(min_row=1, max_row=worksheet.max_row, min_col=1, max_col=1):

        if to_exit:
            break

        for cell in row:
            cell_value = cell.value
            if cell_value is None:
                continue

            if type(cell_value) == int:
                continue

            if 'Total' not in cell_value and 'Reference' not in cell_value:
                continue

            else:
                if 'Reference' in cell_value:
                    reference_cell_coordinate = cell.coordinate
                    reference_cell_row = cell.row
                    reference_cell_column = cell.column

                    days_cell_coordinate = (
                        worksheet.cell(row=reference_cell_row - 1, column=reference_cell_column + 1).coordinate)
                    days_cell_row = reference_cell_row - 1
                    days_cell_column = reference_cell_column + 1

                else:
                    total_cell_coordinate = cell.coordinate  # A404
                    total_cell_row = cell.row  # 404
                    total_cell_column = cell.column  # 1

                    # Fill the result dictionary ---------------------------------------------------
                    counter = 1
                    while 1:
                        current_total_column_cell = worksheet.cell(
                            row=total_cell_row, column=total_cell_column + counter)

                        # check empty -------------------------------------------------------------
                        if current_total_column_cell.value is None:
                            break

                        # sum the values above it -------------------------------------------------
                        current_sum = 0
                        for row in worksheet.iter_rows(min_row=days_cell_row, max_row=total_cell_row - 1,
                                                       min_col=total_cell_column + counter,
                                                       max_col=total_cell_column + counter):
                            for cell in row:
                                if cell.value is None:
                                    continue

                                current_sum += cell.value

                        result[current_total_column_cell.value] = current_sum

    return result
