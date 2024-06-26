// Supposed to show that GO is a staticly and strongly typed language (means that variables must be declared with type and cannot change type)



package main

import "fmt"

func main() {
	var username string = "presidentSkroob"
	var password string = "12345"

	// don't edit below this line
	fmt.Println("Authorization: Basic", username + ":" + password)
}

