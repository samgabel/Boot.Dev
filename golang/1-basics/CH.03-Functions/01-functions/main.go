// We need to declare the parameter types and return type in a function because GO is strongly typed
// We can be more succinct with the typing -> `string` only needs to be declared after s2 because s1 is also a string



package main

import "fmt"

func concat(s1, s2 string) string {
	return s1 + s2
}

// don't touch below this line

func main() {
	test("Lane,", " happy birthday!")
	test("Elon,", " hope that Tesla thing works out")
	test("Go", " is fantastic")
}

func test(s1 string, s2 string) {
	fmt.Println(concat(s1, s2))
}

