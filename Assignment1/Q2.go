package main

import "fmt"

func main(){
	var arr1 = []string {"A","B"}
	var arr2 = []string {"C","D"}
	
	var output [2][2]string
	for i:=0; i<len(arr2); i++ {
		for j:=0; j<len(arr1); j++ {
			output[i][j] = ""+arr1[j]+arr2[i]	
		}	
	}
	fmt.Println(output)
}