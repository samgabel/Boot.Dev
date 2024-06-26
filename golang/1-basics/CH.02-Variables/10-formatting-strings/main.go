// String interpolation in GO uses `fmt.Printf` (console) `fmt.Sprintf` (return)

// `%v` is used to represent the value that you want to add (default)
// `%s` is used for string
// `%d` is used for integer
// `%f` is used for float
// `%.2f` rounds to 2 decimal places



package main

import "fmt"

func main() {
	const name = "Saul Goodman"
	const openRate = 30.5

	msg := fmt.Sprintf("Hi %s, your open rate is %.1f percent\n", name, openRate)

	// don't edit below this line

	fmt.Print(msg)
}

