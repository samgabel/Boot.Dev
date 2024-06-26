// Shows us the different variable types



package main

import "fmt"

func main() {
	// initialize variables here
	var smsSendingLimit int32
	var costPerSMS float32
	var hasPermission bool
	var username string
	fmt.Printf("%v %.2f %v %q\n", smsSendingLimit, costPerSMS, hasPermission, username)
}
