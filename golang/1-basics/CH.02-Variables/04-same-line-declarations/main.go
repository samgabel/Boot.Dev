// We can define and assign multiple variables on the same line (like Python)



package main

import "fmt"

func main() {
	// declare here
	averageOpenRate, displayMessage := 0.23, "is the average open rate of your messages"

	fmt.Println(averageOpenRate, displayMessage)
}
