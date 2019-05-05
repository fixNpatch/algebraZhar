def supportCrypt(source, key, obj):
    source_pointer = 0
    string_counter = 0

    table = []
    key_base = []

    # заполняем табличку
    for i in range(0, len(key)):
        tmp_string = []
        for j in range(0, len(key) - i):
            if source_pointer >= len(source):
                break
            tmp_string.append(source[source_pointer])
            source_pointer += 1
        if not tmp_string:
            break
        table.append(tmp_string)
        string_counter += 1
        if len(source) < len(key):
            break

    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    # блоки отрисовки
    # ~~~~~~~~~~~~~~~~~~~~~

    # рисуем ключ в консоль
    obj.ConsoleLog("Заполненая таблица\n")
    for i in range(0, len(key)):
        obj.ConsoleLog(str(key[i]) + " ")
    obj.ConsoleLog("<--- ключ\n")

    #  рисуем таблицу в консоль
    for i in range(0, string_counter):  # НЦ от 0 до количества строк в таблице
        adj_string = ""
        current_string = table[i]
        for j in range(0, len(current_string)):
            adj_string += str(current_string[j]) + " "
        obj.ConsoleLog(adj_string + '\n')

    # ~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~

    # создаем структуру типа [Буква, Начальная позиция, Колонка]

    for i in range(0, len(table[0])):
        tmp_string = []
        for j in range(0, string_counter):
            if len(table[j]) > i:
                tmp_string.append(table[j][i])
            else:
                break
        key_base.append([str(key[i]), i, tmp_string])

    key_base_sorted = sorted(key_base)

    # инициализируем предварительный результат
    pre_result = ""

    for i in range(0, len(key_base_sorted)):
        tmp_string = ""
        tmp_string_log = ""
        current_column = key_base_sorted[i][2]
        for j in range(0, len(current_column)):
            tmp_string += current_column[j]
            tmp_string_log += str(current_column[j]) + " "
        obj.ConsoleLog("[" + tmp_string_log + "]")
        pre_result += tmp_string
    obj.ConsoleLog("<--- выписываем\n")
    return pre_result


def supportDeCrypt(source, key, obj):
    source_counter = 0
    string_counter = 0

    table = []
    key_base = []

    # заполняем табличку
    for i in range(0, len(key)):
        tmp_string = []
        for j in range(0, len(key) - i):
            if source_counter >= len(source):
                break
            tmp_string.append([])
            source_counter += 1
        if not tmp_string:
            break
        table.append(tmp_string)
        string_counter += 1
        if len(source) < len(key):
            break

    # блок отрисовки
    obj.ConsoleLog("Шаблонная таблица\n")
    for i in range(0, string_counter):
        obj.ConsoleLog(str(table[i]) + '\n')

    # создаем структуру типа [Буква, Начальная позиция, Колонка]
    for i in range(0, len(table[0])):
        tmp_string = []
        for j in range(0, string_counter):
            if len(table[j]) > i:
                tmp_string.append(table[j][i])
            else:
                break
        key_base.append([str(key[i]), i, tmp_string])

    for i in range(0, len(key_base)):
        print(key_base[i])

    # сортируем по алфавиту "столбцы" (вернее уже транспонированные в строки)
    key_sorted = sorted(key_base)

    for i in range(0, len(key_sorted)):
        print(key_sorted[i])

    # заполняем шаблонную таблицу.
    counter = 0
    for i in range(0, len(key_base)):
        stop = False
        for j in range(0, len(key_sorted[i][2])):
            key_sorted[i][2][j] = source[counter]
            counter += 1
            if counter <= 0:
                stop = True
                break
        if stop:
            break

    # сортируем ключ по начальному состоянию
    for i in range(0, len(key_sorted)):
        for j in range(0, len(key_sorted)):
            if key_sorted[i][1] < key_sorted[j][1]:
                key_sorted[i], key_sorted[j] = key_sorted[j], key_sorted[i]

    result = ""
    obj.ConsoleLog("Заполненая таблица\n")
    for i in range(0, len(key)):
        obj.ConsoleLog(str(key[i]) + " ")
    obj.ConsoleLog("<--- ключ\n")

    for i in range(0, len(table)):
        tmp_string = []
        for j in range(0, len(table[i])):
            tmp_string.append(key_sorted[j][2][i])
            result += str(key_sorted[j][2][i])
        # отрисовка
        adj_string = ""
        for c in range(0, len(tmp_string)):
            adj_string += str(tmp_string[c]) + " "
        obj.ConsoleLog(adj_string + "\n")

    print(result)
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
        if 'А' <= source[i] <= 'Я' or '0' < source[i] < '9':
            request.append(source[i])
    source = request

    # переопределение ключа
    request = []
    for i in range(0, len(key)):
        if 'А' <= key[i] <= 'Я' or '0' < key[i] < '9':
            request.append(key[i])
    key = request

    MAX_CHARS = 0
    for i in range(0, len(key)):
        MAX_CHARS += len(key) - i

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
        if 'А' <= source[i] <= 'Я' or '0' < source[i] < '9':
            request.append(source[i])
    source = request

    # переопределение ключа
    request = []
    for i in range(0, len(key)):
        if 'А' <= key[i] <= 'Я' or '0' < key[i] < '9':
            request.append(key[i])
    key = request

    MAX_CHARS = 0
    for i in range(0, len(key)):
        MAX_CHARS += len(key) - i

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
