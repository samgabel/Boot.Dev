package main

import "fmt"

func main() {
	/*
	chose either of these, one is setting the first one sets the `cap` of the underlying array to 3 and the other to 4
	if you append to the array with 3 values it will have to create and new underlying array to accomodate the extra value
	*/

	a := make([]int, 3)
	// a := make([]int, 3, 4)

	fmt.Println("--------A--------")
	fmt.Printf("CAP: %v\n", cap(a))
	fmt.Printf("ADDR: %v\n", &a[0])
	fmt.Printf("ARRAY: %v\n", a)
	fmt.Println()

	bapp := 5
	b := append(a, bapp)
	fmt.Println("--------B--------")
	fmt.Printf("CAP: %v\n", cap(b))
	fmt.Printf("ADDR: %v\n", &b[0])
	fmt.Printf("APPEND: %v\n", bapp)
	fmt.Printf("ARRAY: %v\n", b)
	fmt.Println()

	capp := 6
	c := append(a, capp)
	fmt.Println("--------C--------")
	fmt.Printf("CAP: %v\n", cap(c))
	fmt.Printf("ADDR: %v\n", &c[0])
	fmt.Printf("APPEND: %v\n", capp)
	fmt.Printf("ARRAY: %v\n", c)
	fmt.Println()

	a = append(a, 3)

	fmt.Println("------------------FINAL------------------")
	fmt.Println("A:", a, "|", "B:", b, "|", "C:", c)
}

