# def _FindAnagram(source):
#     source = source.rstrip("\n\r")
#     if len(source) <= 1:
#         return "Нет анаграммы"
#     number = ""
#     number_alp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     for i in range(0, len(source)):
#         if '0' <= str(source[i]) <= '9':
#             number += source[i]
#             number_alp[int(source[i])] += 1
#
#     sav = []
#     current_try = []
#
#     for i in range(0, len(number)):
#         sav.append(number[i])
#         current_try.append(number[i])
#
#     print("sav:", sav)
#
#     counter = 0
#     for i in range(0, len(current_try)):
#         for j in range(0, len(current_try)):
#             if current_try[i] < current_try[j]:
#                 current_try[i], current_try[j] = current_try[j], current_try[i]
#                 counter += 1
#
#     print("sorted:", current_try)
#
#     for i in range(0, len(current_try)):
#         print("now I'm look at ", current_try[i], "(index ", i, ")")
#         if current_try[i] == sav[i]:
#             print("seems not good. try to trade with another index")
#             flag = False
#
#             print("~~~~~~~~~~~~~~~~ try lower ~~~~~~~~~~~~~~~~ ")
#             for j in range(min(i + 1, len(current_try) - 1), len(current_try)):
#                 print("try ", current_try[j], "(index ", j, ") #### comparing with ", current_try[i], "(index ", i, ")",
#                       current_try)
#                 if current_try[i] != current_try[j] and current_try[i] != sav[j] and current_try[j] != sav[i]:
#                     current_try[i], current_try[j] = current_try[j], current_try[i]
#                     counter += 1
#                     flag = True
#                     print("swap")
#                     break
#
#             if flag:
#                 continue
#
#             print("~~~~~~~~~~~~~~~~ try upper ~~~~~~~~~~~~~~~~ ")
#             for j in range(1, i):
#                 index = (i - j)
#                 print("try ", current_try[index], "(index ", index, ") #### comparing with ", current_try[i], "(index ",
#                       i, ")", current_try)
#                 if current_try[i] != current_try[index] and current_try[i] != sav[index] and current_try[index] != sav[
#                     i]:
#                     current_try[i], current_try[index] = current_try[index], current_try[i]
#                     counter += 1
#                     print("swap")
#                     counter += 1
#                     break
#         else:
#             print("this number in good position")
#
#     if counter == 0:
#         return "Нет анаграммы"
#     print("result", current_try)
#
#     number = ""
#     for i in range(0, len(current_try)):
#         number += str(current_try[i])
#
#     return number
#
#
# def FindAnagram(source):
#     source = source.rstrip("\n\r")
#     if len(source) <= 1:
#         return "Нет анаграммы"
#     number = ""
#     number_alp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     for i in range(0, len(source)):
#         if '0' <= str(source[i]) <= '9':
#             number += source[i]
#             number_alp[int(source[i])] += 1
#
#     sav = []
#     current_try = []
#
#     for i in range(0, len(number)):
#         sav.append(number[i])
#         current_try.append(number[i])
#
#     print("sav:", sav)
#
#     counter = 0
#     for i in range(0, len(current_try)):
#         for j in range(0, len(current_try)):
#             if current_try[i] < current_try[j]:
#                 current_try[i], current_try[j] = current_try[j], current_try[i]
#                 counter += 1
#
#     print("sorted:", current_try)
#
#     for i in range(0, len(current_try)):
#         print("now I'm look at ", current_try[i], "(index ", i, ")")
#         if current_try[i] == sav[i]:
#             print("seems not good. try to trade with another index")
#             flag = False
#
#             print("~~~~~~~~~~~~~~~~ try lower ~~~~~~~~~~~~~~~~ ")
#             for j in range(min(i + 1, len(current_try) - 1), len(current_try)):
#                 print("try ", current_try[j], "(index ", j, ") #### comparing with ", current_try[i], "(index ", i, ")",
#                       current_try)
#                 if current_try[i] != current_try[j] and current_try[i] != sav[j] and current_try[j] != sav[i]:
#                     current_try[i], current_try[j] = current_try[j], current_try[i]
#                     counter += 1
#                     flag = True
#                     print("swap")
#                     break
#
#             if flag:
#                 continue
#
#             print("~~~~~~~~~~~~~~~~ try upper ~~~~~~~~~~~~~~~~ ")
#             for j in range(1, i):
#                 index = (i - j)
#                 print("try ", current_try[index], "(index ", index, ") #### comparing with ", current_try[i], "(index ",
#                       i, ")", current_try)
#                 if current_try[i] != current_try[index] and current_try[i] != sav[index] and current_try[index] != sav[
#                     i]:
#                     current_try[i], current_try[index] = current_try[index], current_try[i]
#                     counter += 1
#                     print("swap")
#                     counter += 1
#                     break
#         else:
#             print("this number in good position")
#
#     for i in range(0, len(current_try) - 1):
#         if sav[i + 1] != current_try[i] > current_try[i + 1] != sav[i]:
#             current_try[i], current_try[i + 1] = current_try[i + 1], current_try[i]
#
#     if counter == 0:
#         return "Нет анаграммы"
#     print("result", current_try)
#
#     number = ""
#     for i in range(0, len(current_try)):
#         number += str(current_try[i])
#
#     return number


# def mergeResult(source, sav, l, middle, r, tmp):
#     position_left = l
#     position_middle = middle + 1
#     position_buff = 1
#
#     while position_left <= middle and position_middle <= r:
#         if source[position_left] < source[position_middle]:
#             tmp[position_buff] = source[position_left]
#             position_buff += 1
#             position_left += 1
#         else:
#             tmp[position_buff] = source[position_middle]
#             position_buff += 1
#             position_middle += 1
#
#     while position_middle <= r:
#         tmp[position_buff] = source[position_middle]
#         position_middle += 1
#         position_buff += 1
#
#     while position_left <= middle:
#         tmp[position_buff] = source[position_left]
#         position_left += 1
#         position_buff += 1
#
#     for i in range(0, r - l + 1):
#         source[l + i] = tmp[l + i]
#
#     return source, tmp
#
#
# def mergeSearch(stored_number, sav, l, r, tmp):
#     if l < r:
#         middle = (l + r) / 2
#         stored_number, tmp = mergeSearch(stored_number, sav, l, middle, tmp)
#         stored_number, tmp = mergeSearch(stored_number, sav, middle + 1, l, tmp)
#         stored_number, tmp = mergeResult(stored_number, sav, l, middle, r, tmp)
#     return stored_number, tmp


def func(sav, tmp, i, n):
    k = i - 1
    z = k

    while z >= 0:
        if tmp[k] == tmp[i]:
            k -= 1
        z -= 1

    if k < 0:
        print("error: anagram not found")
        return sav, tmp, False

    else:
        flag = True
        tmp[i], tmp[k] = tmp[k], tmp[i]
        if i + 1 < n and sav[i] != tmp[i + 1] < tmp[i] != sav[i + 1]:
            tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]

        if tmp[k] == sav[k]:
            sav, tmp, flag = func(sav, tmp, k, n)
        return sav, tmp, flag


def FindAnagram(source):
    source = source.rstrip("\n\r")
    if len(source) <= 1:
        return "Нет анаграммы"

    stored_number = []
    sav = []

    for i in range(0, len(source)):
        stored_number.append(source[i])
        sav.append(source[i])

    stored_number.sort()

    for i in range(0, len(stored_number)):
        if stored_number[i] == sav[i]:
            r = i + 1
            if r < len(stored_number):
                z = r
                while z < len(stored_number):
                    if stored_number[r] == stored_number[i]:
                        r += 1
                    z += 1
            if r < len(stored_number):
                stored_number[i], stored_number[r] = stored_number[r], stored_number[i]
            else:
                sav, stored_number, flag = func(sav, stored_number, i, len(stored_number))
                if not flag:
                    print("error")

    print(stored_number)

    result = ""
    for i in range(0, len(stored_number)):
        result += str(stored_number[i])

    return result
