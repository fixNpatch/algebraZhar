def supportCrypt(source, key, obj):
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
    obj.ConsoleLog("Заполненая таблица\n")
    key_array = []
    for i in range(0, len(key)):
        key_array.append(str(key[i]))
    obj.ConsoleLog(str(key_array) + "  <--- ключ\n")

    for i in range(0, string_counter):
        print(generated_structs[i])
        obj.ConsoleLog(str(generated_structs[i]) + '\n')

    print("string counter:", string_counter)
    for i in range(0, len(generated_structs[0])):  # берем первую строку
        adj_result = []
        for j in range(0, string_counter):  # бежим по столбцам
            if len(generated_structs[j]) > i:  # если
                adj_result.append(generated_structs[j][i])
            else:
                break
        key_base.append([str(key[i]), i, adj_result])

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
        obj.ConsoleLog(str(current_column) + " ")
        pre_result += adj_result
    obj.ConsoleLog("<--- выписываем\n")
    return pre_result


def supportDeCrypt(source, key, obj):
    # инициализация двумерного массива
    key_base = []
    counter = 0

    key_array = []
    for i in range(0, len(key)):
        key_array.append(str(key[i]))
    obj.ConsoleLog(str(key_array) + "  <--- ключ\n")

    for i in range(0, min(len(key), len(source))):
        key_base.append([str(key[i]), i])

    # сортируем ключ по алфавиту
    key_sorted = sorted(key_base)
    print("key_sorted:", key_sorted)

    key_array_sorted = []
    for i in range(0, len(key_base)):
        key_array_sorted.append(str(key_sorted[i][0]))
    obj.ConsoleLog(str(key_array_sorted) + "  <--- Отсортированный и подогнанный по размеру ключ\n")

    # необходимо узнать количество строк.
    source_counter = len(source)
    string_counter = 0
    while True:
        source_counter -= len(key_base) - string_counter
        string_counter += 1
        if source_counter <= 0:
            break

    print("количество строк в таблице:", string_counter)
    # указываем длинну строк/столбцов
    rest_source = len(source)
    string_capacity = []
    for i in range(0, string_counter):
        string_capacity.append(min(rest_source, len(key) - i))
        rest_source -= len(key) - i

    cnt = 0
    for i in range(0, min(len(source), len(key))):
        adj_result = []
        source_EOF = False

        # необходимо узнать сколько символов "поместится" в столбце
        rest = len(source)
        str_count = 0
        # while True:
        #     if rest - key_sorted[i][1] > 0:
        #         if rest - (len(key) - str_count) > 0:
        #             rest -= len(key) - str_count
        #             str_count += 1
        #         else:
        #             break
        #     else:
        #         break

        for lum in range(0, string_counter):
            if rest - key_sorted[i][1] > 0:
                rest -= len(key) - lum
                str_count += 1
            else:
                break

        # заполняем таблицу
        for j in range(0, min(string_counter, len(key) - key_sorted[i][1])):
        # for j in range(0, min(string_counter, str_count)):
            # print(string_capacity[key_sorted[i][1]])
            if cnt >= len(source):
                source_EOF = True
                break
            if string_capacity[j] <= 0:
                break
            adj_result.append(source[cnt])
            cnt += 1
            string_capacity[j] -= 1
        print(adj_result)
        key_sorted[i].append(adj_result)
        if source_EOF:
            break

    print("YOHOHO")
    print("key_base", key_sorted)

    # сортируем таблицу по изначальному ключу (например, маяк -> (сейчас) акмя -> (делаем) маяк)
    for i in range(0, min(len(key), len(source))):
        for j in range(0, min(len(key), len(source))):
            if key_sorted[i][1] < key_sorted[j][1]:
                key_sorted[i], key_sorted[j] = key_sorted[j], key_sorted[i]

    result = ""
    for j in range(0, string_counter):
        for i in range(0, len(key_sorted)):
            adj_result = ""
            if len(key_sorted[i]) > 2:
                current_column = key_sorted[i][2]
                if len(current_column) > j:
                    result += current_column[j]
                print(current_column)
            result += adj_result

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
    return result


def MainDeCrypt(source, key, obj):
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
        obj.ConsoleLog("part:" + str(i) + "\n")
        print(posFrom, posTo)
        partedSource = source[posFrom:posTo + 1]
        result += supportDeCrypt(partedSource, key, obj)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')
    return result
