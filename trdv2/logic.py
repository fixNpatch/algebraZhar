def _FindAnagram(source):
    source = source.rstrip("\n\r")
    if len(source) <= 1:
        return "Нет анаграммы"
    number = ""
    number_alp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(source)):
        if '0' <= str(source[i]) <= '9':
            number += source[i]
            number_alp[int(source[i])] += 1

    sav = []
    current_try = []

    for i in range(0, len(number)):
        sav.append(number[i])
        current_try.append(number[i])

    print("sav:", sav)

    counter = 0
    for i in range(0, len(current_try)):
        for j in range(0, len(current_try)):
            if current_try[i] < current_try[j]:
                current_try[i], current_try[j] = current_try[j], current_try[i]
                counter += 1

    print("sorted:", current_try)

    for i in range(0, len(current_try)):
        print("now I'm look at ", current_try[i], "(index ", i, ")")
        if current_try[i] == sav[i]:
            print("seems not good. try to trade with another index")
            flag = False

            print("~~~~~~~~~~~~~~~~ try lower ~~~~~~~~~~~~~~~~ ")
            for j in range(min(i + 1, len(current_try) - 1), len(current_try)):
                print("try ", current_try[j], "(index ", j, ") #### comparing with ", current_try[i], "(index ", i, ")",
                      current_try)
                if current_try[i] != current_try[j] and current_try[i] != sav[j] and current_try[j] != sav[i]:
                    current_try[i], current_try[j] = current_try[j], current_try[i]
                    counter += 1
                    flag = True
                    print("swap")
                    break

            if flag:
                continue

            print("~~~~~~~~~~~~~~~~ try upper ~~~~~~~~~~~~~~~~ ")
            for j in range(1, i):
                index = (i - j)
                print("try ", current_try[index], "(index ", index, ") #### comparing with ", current_try[i], "(index ",
                      i, ")", current_try)
                if current_try[i] != current_try[index] and current_try[i] != sav[index] and current_try[index] != sav[
                    i]:
                    current_try[i], current_try[index] = current_try[index], current_try[i]
                    counter += 1
                    print("swap")
                    counter += 1
                    break
        else:
            print("this number in good position")

    if counter == 0:
        return "Нет анаграммы"
    print("result", current_try)

    number = ""
    for i in range(0, len(current_try)):
        number += str(current_try[i])

    return number


def FindAnagram(source):
    source = source.rstrip("\n\r")
    if len(source) <= 1:
        return "Нет анаграммы"
    number = ""
    number_alp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(source)):
        if '0' <= str(source[i]) <= '9':
            number += source[i]
            number_alp[int(source[i])] += 1

    sav = []
    current_try = []

    for i in range(0, len(number)):
        sav.append(number[i])
        current_try.append(number[i])

    print("sav:", sav)

    counter = 0
    for i in range(0, len(current_try)):
        for j in range(0, len(current_try)):
            if current_try[i] < current_try[j]:
                current_try[i], current_try[j] = current_try[j], current_try[i]
                counter += 1

    print("sorted:", current_try)

    for i in range(0, len(current_try)):
        print("now I'm look at ", current_try[i], "(index ", i, ")")
        if current_try[i] == sav[i]:
            print("seems not good. try to trade with another index")
            flag = False

            print("~~~~~~~~~~~~~~~~ try lower ~~~~~~~~~~~~~~~~ ")
            for j in range(min(i + 1, len(current_try) - 1), len(current_try)):
                print("try ", current_try[j], "(index ", j, ") #### comparing with ", current_try[i], "(index ", i, ")",
                      current_try)
                if current_try[i] != current_try[j] and current_try[i] != sav[j] and current_try[j] != sav[i]:
                    current_try[i], current_try[j] = current_try[j], current_try[i]
                    counter += 1
                    flag = True
                    print("swap")
                    break

            if flag:
                continue

            print("~~~~~~~~~~~~~~~~ try upper ~~~~~~~~~~~~~~~~ ")
            for j in range(1, i):
                index = (i - j)
                print("try ", current_try[index], "(index ", index, ") #### comparing with ", current_try[i], "(index ",
                      i, ")", current_try)
                if current_try[i] != current_try[index] and current_try[i] != sav[index] and current_try[index] != sav[
                    i]:
                    current_try[i], current_try[index] = current_try[index], current_try[i]
                    counter += 1
                    print("swap")
                    counter += 1
                    break
        else:
            print("this number in good position")

    for i in range(0, len(current_try) - 1):
        if sav[i + 1] != current_try[i] > current_try[i + 1] != sav[i]:
            current_try[i], current_try[i + 1] = current_try[i + 1], current_try[i]

    if counter == 0:
        return "Нет анаграммы"
    print("result", current_try)

    number = ""
    for i in range(0, len(current_try)):
        number += str(current_try[i])

    return number