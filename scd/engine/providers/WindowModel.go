package providers

import (
	"fmt"
	"github.com/zserge/webview"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

var LocalStorage string

type WindowModel struct{}

func NewWindowModel() *WindowModel {
	return &WindowModel{}
}

func (m *WindowModel) getAssets(src string) string {
	// read file
	dat, err := ioutil.ReadFile(src)
	if err != nil {
		fmt.Println("Error while reading file", err)
	}
	return string(dat)
}

func (m *WindowModel) IndexHTML() string {
	//	return `
	//<!doctype html>
	//<html lang="en">
	//	<head>
	//		<meta charset="UTF-8">
	//		<meta http-equiv="X-UA-Compatible" content="IE=edge">
	//		<link rel="stylesheet" href="http://cdn.webix.com/edge/webix.css" type="text/css">
	//		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css">
	//		<style>` + m.getAssets("engine/resourses/skin.css") + `</style>
	//    	<script src="http://cdn.webix.com/edge/webix.js" type="text/javascript"></script>
	//		<script>` + m.getAssets("engine/resourses/index.js") + `</script>
	//	</head>
	//	<body></body>
	//</html>
	//`

	// OFFLINE USAGE

	return `
		<!doctype html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css">
			<style> ` + m.getAssets("engine/resourses/webix.css") + `</style>
			<style>` + m.getAssets("engine/resourses/skin.css") + `</style>
    	    <script> ` + m.getAssets("engine/resourses/webix.js") + `</script>
			<script>` + m.getAssets("engine/resourses/index.js") + `</script>
		</head>
		<body></body>
	</html>
`

}

func (m *WindowModel) HandleRPC(w *webview.WebView, data *string) {
	wb := *w
	dt := *data
	switch {
	// Close application
	case dt == "close":
		wb.Terminate()
		break

	// Get changed value of text
	case strings.HasPrefix(dt, "push:"):
		logicModel := new(MainLogic)

		parsedData := strings.TrimPrefix(dt, "push:")
		// var jsString string



		fmt.Println("------------------------------------------------------")
		fmt.Println("------------------------------------------------------")
		fmt.Println("------------------------------------------------------")

		fmt.Println("parsedData::", parsedData)
		resultData, param := logicModel.Crypt(&parsedData)

		fmt.Println("------------------------------------------------------")
		fmt.Println("resultData::", resultData)

		//Form JS
		jsString := `$$('resulted_text').setValue('` + resultData + `');
		webix.message('` + param + `');`
		err := wb.Eval(jsString)
		if err != nil {
			log.Println("Catch error::Cannot Eval JS string", err)
			return
		}

		break

		// Get changed value of text
	case strings.HasPrefix(dt, "pull:"):
		logicModel := new(MainLogic)

		paramPlusData := strings.TrimPrefix(dt, "pull:")
		// var jsString string

		var param rune
		for _, r := range []rune(paramPlusData){
			param = r
			break
		}


		fmt.Println("------------------------------------------------------")
		fmt.Println("------------------------------------------------------")
		fmt.Println("------------------------------------------------------")


		stringedParam := string(param)
		parsedData := strings.TrimPrefix(paramPlusData, string(param)+":")
		fmt.Println("param::", stringedParam)
		fmt.Println("parsedData::", parsedData)
		resultData := logicModel.DeCrypt(stringedParam, &parsedData)



		fmt.Println("------------------------------------------------------")
		fmt.Println("resultData::", resultData)

		//Form JS
		jsString := `$$('resulted_text').setValue('` + resultData + `');`
		err := wb.Eval(jsString)
		if err != nil {
			log.Println("Catch error::Cannot Eval JS string", err)
			return
		}

		break

	// Open file
	case dt == "open":
		log.Println("open") // log stamp
		// open Dialog window
		pathFile := wb.Dialog(webview.DialogTypeOpen, 0, "Open file", "") // absolute path to the file
		fmt.Println(pathFile)                                             // print resultedPath

		b, err := ioutil.ReadFile(pathFile) // just pass the file name
		if err != nil {
			fmt.Println("Catch error::Open file::Read", err)
			return
		}

		// Form JS
		jsString := `$$('resulted_text').setValue(` + strconv.Quote(string(b)) + `);`
		err = wb.Eval(jsString)
		if err != nil {
			log.Println("Catch error::Open file::OpenData", err)
			return
		}
		break

	case dt == "save":
		log.Println("save") // log stamp
		// open Dialog window
		pathFile := wb.Dialog(webview.DialogTypeSave, webview.DialogFlagFile, "Save file", "") // absolute path to the file
		fmt.Println(pathFile)
		err := m.saveFile(pathFile)
		if err != nil {
			log.Println("Catch error::Writing file::", err)
			return
		}
		break
	}
}

func (m *WindowModel) saveFile(pathFile string) (err error) {

	data := []byte(LocalStorage)

	// write the whole body at once
	err = ioutil.WriteFile(pathFile, data, 0644)
	if err != nil {
		return err
	}

	fmt.Println("All good, there're no pointer's error")
	return nil
}

func (m *WindowModel) saveToStorage(order []interface{}, data map[string]string) (result string, err error) {
	for i := range order {
		value := "0"
		for j := range data {
			if order[i].(string) == j {
				value = data[j]
			}
		}
		result += order[i].(string) + ":" + value + "   "
	}

	return
}
