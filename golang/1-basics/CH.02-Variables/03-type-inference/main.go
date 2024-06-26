// Type inference is used by the walrus operator `:=`.
// In this case we use 2.00 because we believe that the future values of the variable will be a float



package main

import "fmt"

func main() {
	penniesPerText := 2.00

	// don't edit below this line
	fmt.Printf("The type of penniesPerText is %T\n", penniesPerText)
}

