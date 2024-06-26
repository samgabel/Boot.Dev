// This specifically shows us that we use channels as "tunnels" between goroutines
// channels can only be 'sent to' and 'received from' seperate goroutines



package main

import (
	"time"
)

type email struct {
	body string
	date time.Time
}

func checkEmailAge(emails [3]email) [3]bool {
	isOldChan := make(chan bool)

	// we need to specify a new goroutine in order to receive from a channel
	// otherwise we get a 'deadlock'
	go sendIsOld(isOldChan, emails)

	isOld := [3]bool{}
	// receiving a value from a channel will 'block' until there is a value in the channel to be read
	// this means that in the `sensIsOld()` function below, we will block at `isOldChan <- true` until the array values (isOld[0]) are populated
	isOld[0] = <-isOldChan
	isOld[1] = <-isOldChan
	isOld[2] = <-isOldChan
	return isOld
}

// don't touch below this line

func sendIsOld(isOldChan chan<- bool, emails [3]email) {
	for _, e := range emails {
		if e.date.Before(time.Date(2020, 0, 0, 0, 0, 0, 0, time.UTC)) {
			isOldChan <- true
			continue
		}
		isOldChan <- false
	}
}

