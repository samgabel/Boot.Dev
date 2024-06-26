// We can use the short assignment statement (walrus operator) `:=` in order to declare variables without having to specify type (type is inferred)



package main

import "fmt"

func main() {
	// declare here
	messageStart := "Happy birthday! You are now"
	age := 21
	messageEnd := "years old!"
	// don't edit below this line
	fmt.Println(messageStart, age, messageEnd)
}
