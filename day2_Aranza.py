def filter_input():
    reports = []
    with open('./input2.txt', encoding='utf-8') as file_handler:
        for line in file_handler:
            string_levels = line.split(" ")
            print(string_levels)
            int_levels = []
            for level in string_levels:
                if ((level != '') or (level != '\n')):
                    int_levels.append(int(level))
            print(int_levels)
            reports.append(int_levels)
    
    return reports     

def is_ascending(a: int, b: int) -> bool:
    return a < b

def check_ascending(a: int, b: int, ascending: bool) -> bool:
    if ascending:
        return a < b
    return a > b

def calculate_safety_of_report(levels: list) -> bool:
    if (len(levels) == 0):
        return False
    if (len(levels) == 1):
        return False

    ascending = is_ascending(levels[0], levels[1])
    size_of_list = len(levels)
    for level_index in range(size_of_list):
        if level_index == size_of_list - 1:
            break
        if not check_ascending(levels[level_index], levels[level_index + 1], ascending):
            return False
        if not check_difference(levels[level_index], levels[level_index + 1]):
            return False
    return True

def check_difference(a: int, b: int) -> bool:
    abs_difference = abs(a-b)
    if abs_difference < 1:
        return False
    if abs_difference > 3:
        return False
    return True

def get_number_of_safe_reports(reports: list) -> int:
    number_of_safe_reports = 0
    for report in reports:
        if calculate_safety_of_report(report):
            number_of_safe_reports += 1
    return number_of_safe_reports


def main():
    safe_reports = get_number_of_safe_reports(filter_input())
    print(safe_reports)


if __name__ == "__main__":
    main()