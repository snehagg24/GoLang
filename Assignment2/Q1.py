package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"log"
	"strings"
	"errors"
	"bufio"
	)

var path = "test.txt"

func createFile() {
	var _, err = os.Stat(path)

	// create file if not exists
	if os.IsNotExist(err) {
		var file, err = os.Create(path)
		if isError(err) { return }
		defer file.Close()
	}
	fmt.Println("Created file")

	var file, error = os.OpenFile(path, os.O_RDWR, 0644)
	if isError(error) { return }
	defer file.Close()

	// write some text line-by-line to file
	fmt.Println("Enter text to written to file. Enter EOF at the end of text.")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		if scanner.Text() == "EOF" {
			break
		}
		_, error = file.WriteString(scanner.Text()+"\n")
		if isError(error) { return }
	}

	// save changes
	error = file.Sync()
	if isError(error) { return }

	fmt.Println("Done writing to file")
}

func displayFile(){
	// re-open file
	var file, err = os.OpenFile(path, os.O_RDWR, 0644)
	if isError(err) { return }
	defer file.Close()

	// read file, line by line
	var text = make([]byte, 1024)
	var EOF = errors.New("EOF")
	for {
		_, err = file.Read(text)
		
		// break if finally arrived at end of file
		if err == EOF {
			break
		}
		
		// break if error occured
		if err != nil && err != EOF {
			isError(err)
			break
		}
	}
	
	fmt.Println(string(text))
}

func editFile(){
	input, err := ioutil.ReadFile(path)
    if err != nil {
        log.Fatalln(err)
    }
	var matchWord string
	fmt.Println("Enter any word that is present in the line to be replaced:")
	fmt.Scanln(&matchWord)
	var newLine string
	fmt.Println("Enter new line:")
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		newLine = scanner.Text()
		break
	}

    lines := strings.Split(string(input), "\n")

    for i, line := range lines {
        if strings.Contains(line, matchWord) {
            lines[i] = newLine
        }
    }
    output := strings.Join(lines, "\n")
    err = ioutil.WriteFile(path, []byte(output), 0644)
    if err != nil {
        log.Fatalln(err)
    }
}

func saveFile(){
	var file, err = os.OpenFile(path, os.O_RDWR, 0644)
	if isError(err) { return }
	defer file.Close()
	
	// save changes
	err = file.Sync()
	if isError(err) { return }
}

func deleteFile(){
	// delete file
	var err = os.Remove(path)
	if isError(err) { return }

	fmt.Println("Done deleting file")
}

func isError(err error) bool {
	if err != nil {
		fmt.Println(err.Error())
	}

	return (err != nil)
}

func main() {
	
	
	for {
		fmt.Println("1.Create File\n2.Display File\n3.Edit File\n4.Save File\n5.Quit\n6.Delete File")
		var choice int
		fmt.Scanln(&choice)
		
		switch choice {
			case 1:
				createFile()
			case 2:
				displayFile()
			case 3:
				editFile()
			case 4:
				saveFile()
			case 5:
				break
			case 6:
				deleteFile()
		}
		if choice == 5 {
			break
		}
	}
}
