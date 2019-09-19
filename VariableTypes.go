package main

import "fmt"

func main(){
	//static
	var x float64
	x = 20.34
	fmt.Println(x)
	fmt.Printf("x is of type %T\n", x)
	
	//dynamic
	y := 6
	fmt.Println(y)
	fmt.Printf("y is of type %T\n", y)
	
	//mixed
	var a,b,c = 3,4.5,"hello"
	fmt.Println(a)
	fmt.Printf("a is of type %T\n", a)
	fmt.Println(b)
	fmt.Printf("b is of type %T\n", b)
	fmt.Println(c)
	fmt.Printf("c is of type %T\n", c)
}