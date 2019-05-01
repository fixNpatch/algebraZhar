package providers

import (
	"errors"
	"fmt"
	"log"
	"strconv"
	"strings"
)

const ALPHABET_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ,.!?:-0123456789"
const ALPHABET_EN = "ABCD"

type MainLogic struct{}

func (ml *MainLogic) Crypt(param string, data *string) (result string) {
	var currentKey string

	var Data = string(*data)

	for i, r := range []rune(Data){
		fmt.Println()
		fmt.Println("i === ", i ," /// r ===", string(r), " /// param === ", param)

		paramIndex, err := foundIndex(param)
		if err != nil {
			log.Printf("currentKey index:: " + err.Error() + ":: " + param)
			return
		}
		fmt.Println("foundIndex with currentKey:", param, "by index of", paramIndex)


		charIndex, err := foundIndex(string(r))
		if err != nil {
			log.Printf("char index::" + err.Error())
			return
		}
		fmt.Println("foundIndex with char:", string(r), "by index of", charIndex)

		countedIndex := (paramIndex + charIndex) % len([]rune(ALPHABET_EN))

		fmt.Println(`RAW:
		charIndex:` + strconv.Itoa(charIndex) + `
		paramIndex:` + strconv.Itoa(paramIndex) + `
		countedIndex ` + strconv.Itoa(countedIndex))

		currentKey = string([]rune(ALPHABET_EN)[countedIndex])

		fmt.Println("currentKey::",currentKey)
		result += currentKey
		param = currentKey
	}
	return result
}

func (ml *MainLogic) DeCrypt(param string, data *string) (result string) {
	var currentKey string

	var Data = string(*data)

	for i, r := range []rune(Data){
		fmt.Println()
		fmt.Println("i === ", i ," /// r ===", string(r), " /// param === ", param)

		paramIndex, err := foundIndex(param)
		if err != nil {
			log.Printf("currentKey index:: " + err.Error() + ":: " + param)
			return
		}
		fmt.Println("foundIndex with currentKey:", param, "by index of", paramIndex)


		charIndex, err := foundIndex(string(r))
		if err != nil {
			log.Printf("char index::" + err.Error())
			return
		}
		fmt.Println("foundIndex with char:", string(r), "by index of", charIndex)


		var countedIndex int
		if charIndex >= paramIndex {
			countedIndex = charIndex - paramIndex
		} else {
			countedIndex = (len([]rune(ALPHABET_EN)) + charIndex - paramIndex) % len([]rune(ALPHABET_EN))
		}

		//countedIndex := (len([]rune(ALPHABET_RU)) + charIndex - paramIndex) % len([]rune(ALPHABET_RU))

		fmt.Println(`RAW:
		charIndex:` + strconv.Itoa(charIndex) + `
		paramIndex:` + strconv.Itoa(paramIndex) + `
		countedIndex ` + strconv.Itoa(countedIndex))

		currentKey = string([]rune(ALPHABET_EN)[countedIndex])

		fmt.Println("currentKey::",currentKey)
		result += currentKey

		nextIndex := (paramIndex + countedIndex) % len([]rune(ALPHABET_EN))
		param = string([]rune(ALPHABET_EN)[nextIndex])
		fmt.Println("nextIndex(" + strconv.Itoa(nextIndex) + ") with char = " + param)
	}
	return result
}

func foundIndex(char string) (index int, err error){
	for i, r := range []rune(ALPHABET_EN) {
		if strings.ToUpper(char) == string(r){
			return i, nil
		}
	}
	return -1, errors.New("index not found")
}