alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ,.!?:-0123456789"


def findInAlph(char):
    for i in range(0, len(alphabet)):
        if char == alphabet[i]:
            return i
    return -1


def MainCrypt(source, paramNumber):
    source = source.rstrip("\r").upper()  # удаляем linebreaks
    source = source.replace('\n', ' ')
    param = alphabet[paramNumber]
    print(source)
    print(paramNumber)
    result = ""
    for i in range(0, len(source)):
        currentChar = source[i]
        if currentChar == '\n' and i > 0:
            if source[i - 1] == '\n':
                continue
            currentChar = " "
        source_char = findInAlph(str(currentChar))
        if source_char != -1:
            print("!= - 1")
            computedChar = (source_char + findInAlph(str(param))) % len(alphabet)
        else:
            print("-1")
            result = result + source[i]
            continue
        print(source[i], "// index of char:", findInAlph(str(currentChar)), "index of param:", findInAlph(str(param)), "computedChar:", computedChar)
        result = result + alphabet[computedChar]
        param = alphabet[computedChar]
    print(result)
    return result


def MainDeCrypt(source, param):
    source = source.rstrip("\r").upper()  # удаляем linebreaks
    source.replace('\n', ' ')
    print(source)
    print(param)
    param = param.upper()
    result = ""
    for i in range(0, len(source)):
        source_char = findInAlph(str(source[i]))
        if source_char != -1:
            print("!= - 1")
            computedChar = (len(alphabet) + source_char - findInAlph(str(param))) % len(alphabet)
        else:
            print("-1")
            result = result + source[i]
            continue
        print(source[i], "// index of char:", findInAlph(str(source[i])), "index of param:", findInAlph(str(param)),
              "computedChar:", computedChar)
        result = result + alphabet[computedChar]
        param = alphabet[source_char]
    print(result)
    return result
