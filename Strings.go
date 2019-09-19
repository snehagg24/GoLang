package main

import ("fmt"; "strings")

func main() {
   var greeting =  "Hello world!"
   
   fmt.Printf("String Length is: ")
   fmt.Println(len(greeting)) 

   //concatenation
   msg :=  []string{"Hello","world!"}   
   fmt.Println(strings.Join(msg, " "))
   
   
}