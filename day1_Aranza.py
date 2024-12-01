list1 =  []
list2 =  []

with open('./input.txt') as file_handler:
    for line in file_handler:
        result = line.split('   ')
        if (result[0] != ""):
            list1.append(int(result[0]))
        if (result[1] != ""):
            list2.append(int(result[1]))
list1.sort()
list2.sort()
distance = 0
index = 0
similarityindex = 0

listrepeatednumbers = []
for number in list1:
    distance = distance + abs(number - list2[index])
    if (number in list2) & (number not in listrepeatednumbers):
        listrepeatednumbers.append(number)
        repeatedinstances = list2.count(number)
        similarityindex = similarityindex + (number * repeatedinstances)
    index = index + 1


print(index)
print(distance)
print(similarityindex)