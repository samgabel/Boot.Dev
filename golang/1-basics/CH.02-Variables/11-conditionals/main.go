// Conditionals in GO do not use parentheses around the condition, otherwise everything else is the same as javascript



package main

import "fmt"

func main() {
	messageLen := 10
	maxMessageLen := 20
	fmt.Println("Trying to send a message of length:", messageLen, "and a max length of:", maxMessageLen)

	// don't touch above this line

	if messageLen < maxMessageLen {
		fmt.Println("Message sent")
	} else {
		fmt.Println("Message not sent")
	}

	// we could also use the "initial statement" of the `if` statement (this is for conciseness and scoping variables within the `if` statment)

	// if messageLen, maxMessageLen := 10, 20; messageLen < maxMessageLen {
	// 	fmt.Println("Message sent")
	// } else {
	// 	fmt.Println("Message not sent")
	// }
}
