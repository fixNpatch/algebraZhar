def supportCrypt(source, key, obj):
    # нужен для проверки len(source) <? количества ячеек в таблице
    source_counter = 0

    # инициализация двумерного массива
    generated_structs = []

    key_UNIQUE = []
    key_BASE = []

    # собираем уникальный ключ
    for i in range(0, len(key)):
        already_included = False
        for j in range(0, len(key_UNIQUE)):
            if key[i] == key_UNIQUE[j]:
                already_included = True
                break
        if already_included:
            continue
        else:
            key_UNIQUE.append(str(key[i]))

    for i in range(0, len(key)):
        key_BASE.append(str(key[i]))

    for i in range(0, len(key_BASE)):
        adj_result = []
        for j in range(0, len(key_UNIQUE)):
            if source_counter >= len(source):
                adj_result.append("#")
            else:
                adj_result.append(source[source_counter])
                source_counter += 1
        generated_structs.append(adj_result)

    for i in range(0, len(key_BASE)):
        obj.ConsoleLog(str(generated_structs[i]) + "\n")
        print(generated_structs[i])

    result_structs = []

    # транспонируем
    for i in range(0, len(key_UNIQUE)):
        adj_result = []
        for j in range(0, len(key_BASE)):
            adj_result.append(generated_structs[j][i])
        result_structs.append([str(key_UNIQUE[i]), i, adj_result])

    result_structs_sorted = sorted(result_structs)

    result = ""
    for i in range(0, len(key_UNIQUE)):
        for j in range(0, len(result_structs_sorted[i][2])):
            result += result_structs_sorted[i][2][j]

    return result


def supportDeCrypt(source, key, obj):
    source_counter = 0

    # инициализация двумерного массива
    generated_structs = []

    key_UNIQUE = []

    # собираем уникальный ключ
    for i in range(0, len(key)):
        already_included = False
        for j in range(0, len(key_UNIQUE)):
            if key[i] == key_UNIQUE[j]:
                already_included = True
                break
        if already_included:
            continue
        else:
            key_UNIQUE.append(str(key[i]))

    obj.ConsoleLog("Временная(черновая) таблица\n")
    for i in range(0, len(key_UNIQUE)):
        adj_result = []
        for j in range(0, len(key)):
            adj_result.append(source[source_counter])
            source_counter += 1
        obj.ConsoleLog(str(adj_result) + '\n')
        generated_structs.append(adj_result)

    for i in range(0, len(key_UNIQUE)):
        print(generated_structs[i])

    generated_structs_adj = []
    for i in range(0, len(key_UNIQUE)):
        generated_structs_adj.append([str(key_UNIQUE[i]), i, []])

    generated_structs_sorted = sorted(generated_structs_adj)

    for i in range(0, len(key_UNIQUE)):
        generated_structs_sorted[i][2] = generated_structs[i]

    for i in range(0, len(key_UNIQUE)):
        for j in range(0, len(key_UNIQUE)):
            if generated_structs_sorted[i][1] < generated_structs_sorted[j][1]:
                generated_structs_sorted[i], generated_structs_sorted[j] = generated_structs_sorted[j], \
                                                                           generated_structs_sorted[i]
    obj.ConsoleLog("Отсортированная таблица\n")
    for i in range(0, len(key_UNIQUE)):
        print(generated_structs_sorted[i])
        obj.ConsoleLog(str(generated_structs_sorted[i][2]) + '\n')

    result = ""
    obj.ConsoleLog("Восстановленная таблица\n")
    for i in range(0, len(key)):
        adj_result = []
        for j in range(0, len(key_UNIQUE)):
            adj_result.append(str(generated_structs_sorted[j][2][i]))
            result += str(generated_structs_sorted[j][2][i])
        obj.ConsoleLog(str(adj_result) + '\n')

    pointer_left = 0
    while pointer_left < len(result):
        if result[pointer_left] == '#':
            pointer_right = pointer_left
            while pointer_right < len(result) and result[pointer_left] == result[pointer_right]:
                pointer_right += 1
            result = result[:pointer_left] + result[pointer_right:]
        pointer_left += 1

    return result


def MainCrypt(source, key, obj):
    obj.ConsoleLog("Шифрование\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    source = source.rstrip("\n\r").upper()  # удаляем linebreaks
    key = key.rstrip("\n\r").upper()
    source = source.replace('\n', '')
    source = source.replace(' ', '')
    key = key.replace('\n', '')
    key = key.replace(' ', '')
    print("source:\t", source)
    print("key:\t", key)

    # переопределение
    request = []
    for i in range(0, len(source)):
        if 'А' <= source[i] <= 'Я' or '0' < source[i] < '9' or source[i] == '#':
            request.append(source[i])
    source = request

    key_UNIQUE = []
    # собираем уникальный ключ
    for i in range(0, len(key)):
        already_included = False
        for j in range(0, len(key_UNIQUE)):
            if key[i] == key_UNIQUE[j]:
                already_included = True
                break
        if already_included:
            continue
        else:
            key_UNIQUE.append(str(key[i]))

    MAX_CHARS = len(key) * len(key_UNIQUE)

    # разбиваем на куски открытый (исходный) текст
    parts = len(source) // MAX_CHARS
    if len(source) % MAX_CHARS != 0:
        parts = parts + 1
    print("parts:", parts)
    obj.ConsoleLog("Количество блоков:" + str(parts) + "\n")

    pre_result = ""
    posFrom = 0
    posTo = MAX_CHARS - 1
    for i in range(0, int(parts)):
        print(posFrom, posTo)
        obj.ConsoleLog("\tБлок:" + str(i) + '\n')
        partedSource = source[posFrom:posTo + 1]
        pre_result += supportCrypt(partedSource, key, obj)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')

    result = ""

    for i in range(0, len(pre_result)):
        if (i % 5) == 0 and i != 0:
            # result += "\n" # сказала что не надо разбивать на строки
            result += ""
        result += pre_result[i]

    print(result)
    obj.ConsoleLog(" ~~ OK ~~\n\n")
    return result


def MainDeCrypt(source, key, obj):
    obj.ConsoleLog("Дешифрование\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    source = source.rstrip("\n\r").upper()  # удаляем linebreaks
    key = key.rstrip("\n\r").upper()
    source = source.replace('\n', '')
    source = source.replace(' ', '')
    key = key.replace('\n', '')
    key = key.replace(' ', '')
    print("source:\t", source)
    print("key:\t", key)

    # переопределение
    request = []
    for i in range(0, len(source)):
        if 'А' <= source[i] <= 'Я' or '0' < source[i] < '9' or source[i] == '#':
            request.append(source[i])
    source = request

    key_UNIQUE = []
    # собираем уникальный ключ
    for i in range(0, len(key)):
        already_included = False
        for j in range(0, len(key_UNIQUE)):
            if key[i] == key_UNIQUE[j]:
                already_included = True
                break
        if already_included:
            continue
        else:
            key_UNIQUE.append(str(key[i]))

    MAX_CHARS = len(key) * len(key_UNIQUE)

    # разбиваем на куски открытый (исходный) текст
    parts = len(source) // MAX_CHARS
    if len(source) % MAX_CHARS != 0:
        parts = parts + 1
    print("parts:", parts)
    obj.ConsoleLog("Количество блоков:" + str(parts) + "\n")

    result = ""
    posFrom = 0
    posTo = MAX_CHARS - 1
    for i in range(0, int(parts)):
        print(posFrom, posTo)
        obj.ConsoleLog("\tБлок:" + str(i) + '\n')
        partedSource = source[posFrom:posTo + 1]
        result += supportDeCrypt(partedSource, key, obj)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')
    obj.ConsoleLog(" ~~ OK ~~\n\n")
    return result
