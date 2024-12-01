def filter_input():
    list1 = []
    list2 = []
    with open('./input.txt', encoding='utf-8') as file_handler:
        for line in file_handler:
            result = line.split('   ')
            list1.append(int(result[0]))
            list2.append(int(result[1]))
    return list1, list2


def calculate_similarity_index(number: int, list1: list, list2: list, numbersalreadycalculated: list) -> int:
    if number not in list2:
        return 0
    if number in numbersalreadycalculated:
        return 0
    repeatedinstances = list2.count(number)
    similarityindex = number * repeatedinstances
    return similarityindex

def calculate_distance_and_similarity_index(list1: list, list2: list):
    index = 0
    distance = 0
    similarityindex = 0
    listrepeatednumbers = []
    for number in list1:
        distance += abs(number - list2[index])
        index += 1
        calculated_similarity_index = calculate_similarity_index(number, list1, list2, listrepeatednumbers) 
        if calculated_similarity_index == 0:
            continue
        listrepeatednumbers.append(number)
        similarityindex += calculated_similarity_index
    return distance, similarityindex

def main():
    list1, list2 = filter_input()
    list1.sort()
    list2.sort()
    distance, similarityindex = calculate_distance_and_similarity_index(list1, list2)
    print(distance)
    print(similarityindex)

if __name__ == "__main__":
    main()