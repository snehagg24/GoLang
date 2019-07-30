package main

import "fmt"

func main(){
	
	var arr = []string {"Good","Better","Best","Fantastic","Perfect","Super","Fine","Great"}

	firstHalf := arr[0:len(arr)/2]
	secondHalf := arr[len(arr)/2:len(arr)]
	
	var output []string
	for i:= len(firstHalf)-1; i>=0; i-- {
		output = append(output,firstHalf[i])
	}
	for i:= len(secondHalf)-1; i>=0; i-- {
		output = append(output,secondHalf[i])
	}
	fmt.Println(output)
}
