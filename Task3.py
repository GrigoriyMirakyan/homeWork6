line = "пара-ра-рам рам-пам-папам па-ра-па-дам"


def check_line(line):
    lines = line.split()
    list_of_lines = [sum(x in 'аеиоуыэюя' for x in a) for a in lines]
    if len(set(list_of_lines)) == 1:
        result = "Парам пам-пам"
    else:
        result = "Пам парам"
    return result

print(check_line(line))
