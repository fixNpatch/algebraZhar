def AddRevers(A):
    mA = [A[0:2], A[2:4]]
    C = [[0, 0], [0, 0]]
    for i in range(0, len(mA)):
        for j in range(0, len(mA)):
            C[i][j] = mA[(j + 1) % 2][(i + 1) % 2]
    c = []
    for i in range(0, len(C)):
        for j in range(0, len(C)):
            c.append(C[i][j])
    return c


def Additio(A, B, mod):
    C = []
    for i in range(0, len(A)):
        C.append((A[i] + B[i]) % mod)
    return C


def Multiplic(A, B, mod):
    C = [[0, 0], [0, 0]]
    mA = [A[0:2], A[2:4]]
    mB = [B[0:2], B[2:4]]

    # for i in range(0, len(mA)):
    #     for j in range(0, len(mA[i])):
    #         C[j][i] = (
    #                           mA[i][j] * mB[i][j] +
    #                           mA[(j + 1) % 2][i] * mB[i][(j + 1) % 2]
    #                 ) % mod

    r = 0
    for i in range(0, len(mA)):
        for j in range(0, len(mA[i])):
            C[i][j] = (
                              mA[i][r] * mB[r][j] +
                              mA[i][r + 1] * mB[r + 1][j]
                      ) % mod

    c = []
    for i in range(0, len(C)):
        for j in range(0, len(C)):
            c.append(C[i][j])
    return c


# # считаем определитель
# def CountDelta(A):
#     mA = [A[0:2], A[2:4]]
#     return mA[0][0] * mA[1][1] - mA[0][1] * mA[1][0]
#
#
# def FindMultiplReverse(A):
#     mA = [A[0:2], A[2:4]]
#     mA_ = [[0, 0], [0, 0]]
#     mAr = []
#
#     for i in range(0, 2):
#         for j in range(0, 2):
#             number = mA[(i + 1) % 2][(j + 2) % 2]
#             if i == 1 or j == 1:
#                 number *= -1
#             mA_[i][j] = number
#
#     delta = CountDelta(A)
#
#     for i in range(0, 2):
#         for j in range(0, 2):
#             mAr.append(mA_[i][j] / delta)
#     return mAr


def charachteristix(result, add, reach):
    if result == [0, 0, 0, 0] or reach > 100:
        return reach
    else:
        return charachteristix(Additio(result, add, 5), add, reach + 1)


def MainCheck(path, obj):
    print(path)
    obj.ConsoleLog("Opened file: " + path + "\n\n")
    BIGBAD = False

    # необходимо проверить все аксиомы и убедиться что это поле
    # вывести промежуточный результат проверки
    # затем проверить поле о характеристике 5

    # проверка осуществляется: единичный элемент ( в данном случае матрица) складывается 5 раз
    # можно заметить что все числа взяты по модулю 5
    # значит при сложении единичной матрицы 5 раз (элементы в матрице складываем по модулю) у нас получается нулевая матрица.

    F = []
    AdditionalNeutral = []
    MultiplicalNeutral = []

    file = open(path, "r")
    for line in file:
        matrix = []
        for char in line:
            if '0' <= char <= '9':
                matrix.append(int(char))
        # закидываем матрицу во множество
        F.append(matrix)

    # аксиомы поля
    # a + b = b + a
    # (a + b) + c = a + (b + c)
    # a + 0 = 0 + a = a
    # a + (-a) = (-a) + a = 0
    # a * b = b * a
    # (a * b) * c = a * (b * c)
    # a * 1 = 1 * a = a
    # a * (A) = (A) * a = 1 | a != 0
    # a * (b + c) = a * b + a * c

    badWithAdditio = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            cycled = False
            for k in range(0, len(F)):
                if F[k] == Additio(F[i], F[j], 5):
                    cycled = True
                    break
            if not cycled:
                badWithAdditio = True
    if badWithAdditio:
        obj.ConsoleLog("Множество НЕ замкнуто относительно сложения\n")
    else:
        obj.ConsoleLog("Множество замкнуто относительно сложения\n")

    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    badWithMulti = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            cycled = False
            for k in range(0, len(F)):
                if F[k] == Multiplic(F[i], F[j], 5):
                    cycled = True
                    break
            if not cycled:
                badWithMulti = True
    if badWithMulti:
        obj.ConsoleLog("Множество НЕ замкнуто относительно умножения\n")
    else:
        obj.ConsoleLog("Множество замкнуто относительно умножения\n")
    obj.ConsoleLog("\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    bad = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            if i == j:
                continue
            AB = Additio(F[i], F[j], 5)
            BA = Additio(F[j], F[i], 5)
            if AB != BA:
                bad = True
                break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a + b = b + a\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a + b = b + a\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            for k in range(0, len(F)):
                if i == j:
                    continue
                AB = Additio(Additio(F[i], F[j], 5), F[k], 5)
                BA = Additio(F[i], Additio(F[j], F[k], 5), 5)
                if AB != BA:
                    bad = True
                    break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома (a + b) + c = a + (b + c)\n")
    else:
        obj.ConsoleLog("Выполнена аксиома (a + b) + c = a + (b + c)\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = True
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            AB = Additio(F[i], F[j], 5)
            BA = Additio(F[j], F[i], 5)
            if AB == BA and AB == F[i]:
                AdditionalNeutral = F[j]
                bad = False
                break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a + 0 = 0 + a = a\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a + 0 = 0 + a = a\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = False
    for i in range(0, len(F)):
        Exist = False
        for j in range(0, len(F)):
            if i == j:
                continue
            AB = Additio(F[i], F[j], 5)
            BA = Additio((F[j]), F[i], 5)
            if AB == BA == [0, 0, 0, 0] or F[i] == [0, 0, 0, 0]:
                Exist = True
                continue
        if not Exist:
            bad = True
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a + (-a) = (-a) + a = 0\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a + (-a) = (-a) + a = 0\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            if i == j:
                continue
            AB = Multiplic(F[i], F[j], 5)
            BA = Multiplic(F[j], F[i], 5)
            if AB != BA:
                bad = True
                break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a * b = b * a\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a * b = b * a\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            for k in range(0, len(F)):
                AB = Multiplic(Multiplic(F[i], F[j], 5), F[k], 5)
                BA = Multiplic(F[i], Multiplic(F[j], F[k], 5), 5)
                if AB != BA:
                    bad = True
                    break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома (a * b) * c = a * (b * c)\n")
    else:
        obj.ConsoleLog("Выполнена аксиома (a * b) * c = a * (b * c)\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    # bad = True
    # for i in range(0, len(F)):
    #     for j in range(0, len(F)):
    #         if i == j:
    #             continue
    #         AB = Multiplic(F[i], F[j], 5)
    #         BA = Multiplic(F[j], F[i], 5)
    #         if AB == BA and AB == F[i]:
    #             MultiplicalNeutral = F[j]
    #             bad = False
    #             break
    # if bad:
    #     BIGBAD = True
    #     obj.ConsoleLog("Не выполнена аксиома a * 1 = 1 * a = a\n")
    # else:
    #     obj.ConsoleLog("Выполнена аксиома a * 1 = 1 * a = a\n")
    #

    bad = True
    for i in range(0, len(F)):
        cnt = 0
        for j in range(0, len(F)):
            if i == j:
                continue
            AB = Multiplic(F[j], F[i], 5)
            BA = Multiplic(F[i], F[j], 5)
            if AB == BA and AB == F[j]:
                cnt += 1
        if cnt == len(F) - 1:
            MultiplicalNeutral = F[i]
            bad = False
            break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a * 1 = 1 * a = a\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a * 1 = 1 * a = a\n")

    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = False
    for i in range(0, len(F)):
        Exist = False
        for j in range(0, len(F)):
            AB = Multiplic(F[i], F[j], 5)
            BA = Multiplic((F[j]), F[i], 5)
            if AB == BA and (AB == MultiplicalNeutral or F[i] == AdditionalNeutral):
                Exist = True
                continue
        if not Exist:
            bad = True
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a * (A) = (A) * a = 1\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a * (A) = (A) * a = 1\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------
    bad = False
    for i in range(0, len(F)):
        for j in range(0, len(F)):
            if i == j:
                continue
            for k in range(0, len(F)):
                if k == j or k == i:
                    continue
                AB = Multiplic(F[i], Additio(F[j], F[k], 5), 5)
                BA = Additio(Multiplic(F[i], F[j], 5), Multiplic(F[i], F[k], 5), 5)
                if AB != BA:
                    bad = True
                    break
    if bad:
        BIGBAD = True
        obj.ConsoleLog("Не выполнена аксиома a * (b + c) = a * b + a * c\n")
    else:
        obj.ConsoleLog("Выполнена аксиома a * (b + c) = a * b + a * c\n")
    # -----------------------------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------

    obj.ConsoleLog("\n")
    if AdditionalNeutral:
        obj.ConsoleLog("Нейтральный элемент по сложению: " + str(AdditionalNeutral) + "\n")
    else:
        obj.ConsoleLog("Нет нейтрального элемента по сложению\n")

    if MultiplicalNeutral:
        obj.ConsoleLog("Нейтральный элемент по умножению: " + str(MultiplicalNeutral) + "\n")
    else:
        obj.ConsoleLog("Нет нейтрального элемента по умножению\n")


    obj.ConsoleLog("\n")

    obj.ConsoleLog("Проверяем на характеристику N\n")
    reach = charachteristix([1, 0, 0, 1], [1, 0, 0, 1], 0)
    obj.ConsoleLog("Характеристика: " + str(reach + 1))

    # определяем конечный результат
    if not BIGBAD:
        obj.ConsoleLog("\nВывод: Данное множество является полем характеристики " + str(reach + 1))
    else:
        obj.ConsoleLog("\nВывод: Данное множество НЕ является полем")


    return ""
