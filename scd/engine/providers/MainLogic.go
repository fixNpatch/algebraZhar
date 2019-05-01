package providers

import (
	"errors"
	"fmt"
	"log"
	"math/rand"
	"strconv"
	"strings"
)

const ALPHABET_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ,.!?:-0123456789"
const ALPHABET_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

type MainLogic struct{}

func (ml *MainLogic) Crypt(data *string) (result string, paramReturn string) {
	var currentKey string

	fmt.Println(ALPHABET_RU, len([]rune(ALPHABET_RU)))
	var startKey = rand.Intn(51)
	paramReturn = string([]rune(ALPHABET_RU)[startKey])
	param := paramReturn

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

		countedIndex := (paramIndex + charIndex) % len([]rune(ALPHABET_RU))

		fmt.Println(`RAW:
		charIndex:` + strconv.Itoa(charIndex) + `
		paramIndex:` + strconv.Itoa(paramIndex) + `
		countedIndex ` + strconv.Itoa(countedIndex))

		currentKey = string([]rune(ALPHABET_RU)[countedIndex])

		fmt.Println("currentKey::",currentKey)
		result += currentKey
		param = currentKey
	}
	return result, paramReturn
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
			countedIndex = (len([]rune(ALPHABET_RU)) + charIndex - paramIndex) % len([]rune(ALPHABET_RU))
		}

		//countedIndex := (len([]rune(ALPHABET_RU)) + charIndex - paramIndex) % len([]rune(ALPHABET_RU))

		fmt.Println(`RAW:
		charIndex:` + strconv.Itoa(charIndex) + `
		paramIndex:` + strconv.Itoa(paramIndex) + `
		countedIndex ` + strconv.Itoa(countedIndex))

		currentKey = string([]rune(ALPHABET_RU)[countedIndex])

		fmt.Println("currentKey::",currentKey)
		result += currentKey

		nextIndex := (paramIndex + countedIndex) % len([]rune(ALPHABET_RU))
		param = string([]rune(ALPHABET_RU)[nextIndex])
		fmt.Println("nextIndex(" + strconv.Itoa(nextIndex) + ") with char = " + param)
	}
	return result
}

func foundIndex(char string) (index int, err error){
	for i, r := range []rune(ALPHABET_RU) {
		if strings.ToUpper(char) == string(r){
			return i, nil
		}
	}
	return -1, errors.New("index not found")
}