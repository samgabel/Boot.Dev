// Constants can either be declared immedietly or "computed".
// Computed meaning "happening at compile time" (we cannot declare constants that are declared at run-time)



package main

import "fmt"

func main() {
	const secondsInMinute = 60
	const minutesInHour = 60
	const secondsInHour = secondsInMinute * minutesInHour

	// don't edit below this line
	fmt.Println("number of seconds in an hour:", secondsInHour)
}

