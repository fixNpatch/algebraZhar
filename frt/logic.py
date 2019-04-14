def supportCrypt(source, key):
    # нужен для проверки len(source) <? количества ячеек в таблице
    source_counter = 0
    # нужен для проверки сколько получилось строк
    string_counter = 0

    # инициализация двумерного массива
    generated_structs = []
    key_base = []

    print("parted source:", key)

    # заполняем табличку
    for i in range(0, len(key)):
        adj_result = []  # промежуточный результат (набираем строку, чтобы потом запушить в таблицу)
        for j in range(0, len(key) - i):
            if source_counter >= len(source):
                break
            adj_result.append(source[source_counter])
            source_counter += 1
        if not adj_result:
            break
        generated_structs.append(adj_result)
        string_counter += 1
        if len(source) < len(key):
            break
    print("заполненая таблица")
    for i in range(0, string_counter):
        print(generated_structs[i])


    if len(source) > len(key):
        # транспонируем таблицу для дальнейший манипуляций с данными
        for i in range(0, len(key)):
            adj_result = []
            for j in range(0, len(generated_structs[i])):
                adj_result.append(generated_structs[j][i])
            key_base.append([str(key[i]), i, adj_result])
    else:
        for i in range(0, len(generated_structs[0])):
            key_base.append([str(key[i]), i, generated_structs[0][i]])

    # # транспонируем таблицу для дальнейший манипуляций с данными
    # for i in range(0, len(generated_structs)):
    #     adj_result = []
    #     for j in range(0, len(generated_structs[i])):
    #         adj_result.append(generated_structs[j][i])
    #     print(adj_result)
    #     key_base.append([str(key[i]), i, adj_result])

    print("key_base:", key_base)

    # инициализируем предварительный результат
    pre_result = ""

    # сортируем по алфавиту "столбцы" (вернее уже транспонированные в строки)
    key_sorted = sorted(key_base)
    for i in range(0, len(key_sorted)):
        adj_result = ""
        current_column = key_sorted[i][2]
        for j in range(0, len(current_column)):
            adj_result += current_column[j]
        print(current_column)
        pre_result += adj_result

    result = ""

    for i in range(0, len(pre_result)):
        if (i % 5) == 0 and i != 0:
            result += "\n"
        result += pre_result[i]
    return result


def supportDeCrypt(source, key):
    # инициализация двумерного массива
    key_base = []
    counter = 0

    for i in range(0, len(key)):
        key_base.append([str(key[i]), i])

    # сортируем ключ по алфавиту
    key_sorted = sorted(key_base)
    print("key_sorted:", key_sorted)

    for i in range(0, len(key_sorted)):
        adj_result = []
        for j in range(0, len(key_sorted) - key_sorted[i][1]):
            if counter >= len(source):
                break
            adj_result.append(str(source[counter]))
            counter += 1
        key_sorted[i].append(adj_result)
        if counter >= len(source):
            break

    print("before transp:", key_sorted)
    print("key_base", key_base)

    result = ""


    # необходимо транспонирование
    for i in range(0, len(key_base)):
        for j in range(0, len(key_base[i][2])):
            result += key_base[j][2][i]
    return result


def MainCrypt(source, key):
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

    MAX_CHARS = 0
    for i in range(0, len(key)):
        MAX_CHARS += len(key) - i

    # разбиваем на куски открытый (исходный) текст
    parts = len(source) // MAX_CHARS
    if len(source) % MAX_CHARS != 0:
        parts = parts + 1
    print("parts:", parts)

    result = ""
    posFrom = 0
    posTo = MAX_CHARS - 1
    for i in range(0, int(parts)):
        print(posFrom, posTo)
        partedSource = source[posFrom:posTo + 1]
        result += supportCrypt(partedSource, key)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')

    return result


def MainDeCrypt(source, key):
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

    MAX_CHARS = 0
    for i in range(0, len(key)):
        MAX_CHARS += len(key) - i

    # разбиваем на куски открытый (исходный) текст
    parts = len(source) // MAX_CHARS
    if len(source) % MAX_CHARS != 0:
        parts = parts + 1
    print("parts:", parts)

    result = ""
    posFrom = 0
    posTo = MAX_CHARS - 1
    for i in range(0, int(parts)):
        print(posFrom, posTo)
        partedSource = source[posFrom:posTo + 1]
        result += supportDeCrypt(partedSource, key)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')
    return result
