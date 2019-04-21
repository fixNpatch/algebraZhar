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
        pre_result += adj_result

    return pre_result


def supportDeCrypt(source, key):
    # инициализация двумерного массива
    key_base = []
    counter = 0

    for i in range(0, len(key)):
        key_base.append([str(key[i]), i])

    # сортируем ключ по алфавиту
    key_sorted = sorted(key_base)
    print("key_sorted:", key_sorted)

    # необходимо узнать количество строк.
    source_counter = len(source)
    string_counter = 0
    while True:
        source_counter -= len(key) - string_counter
        string_counter += 1
        if source_counter <= 0:
            break

    # указываем длинну строк/столбцов
    rest_source = len(source)
    string_capacity = []
    for i in range(0, string_counter):
        string_capacity.append(min(rest_source, len(key) - i))
        rest_source -= len(key) - i

    print("string_capacity")
    for i in range(0, string_counter):
        print(string_capacity[i])

    cnt = 0
    for i in range(0, min(len(source), len(key))):
        adj_result = []
        flag = False
        print(len(key) - key_sorted[i][1])
        for j in range(0, min(string_counter, len(key) - key_sorted[i][1])):
            if cnt >= len(source):
                flag = True
                break
            if string_capacity[j] <= 0:
                break
            adj_result.append(source[cnt])
            cnt += 1
            string_capacity[j] -= 1
        key_sorted[i].append(adj_result)
        if flag:
            break

    print("key_base", key_sorted)

    for i in range(0, len(key)):
        for j in range(0, len(key)):
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

    print("sorted", result)

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

    pre_result = ""
    posFrom = 0
    posTo = MAX_CHARS - 1
    for i in range(0, int(parts)):
        print(posFrom, posTo)
        partedSource = source[posFrom:posTo + 1]
        pre_result += supportCrypt(partedSource, key)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')

    result = ""

    for i in range(0, len(pre_result)):
        if (i % 5) == 0 and i != 0:
            result += "\n"
        result += pre_result[i]

    print(result)
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
        print(posFrom, posTo)
        partedSource = source[posFrom:posTo + 1]
        result += supportDeCrypt(partedSource, key)
        posFrom = posFrom + MAX_CHARS
        posTo = min(len(source), posTo + MAX_CHARS)

    print('\n\n ~~ OK ~~\n')
    return result
