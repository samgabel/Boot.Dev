// This shows us how channels can be used to send signals or 'tokens' (called "signal channels").



package main

import "fmt"

func waitForDBs(numDBs int, dbChan chan struct{}) {
	// we need to receive from the channel, until nothing is being sent to the channel
	// otherwise the goroutine *receiving* the channel will be blocked
	// without this for loop, the necessary amount of 'receives' is not met
	for i := 0; i < numDBs; i++ {
		// we don't care what is being passed through the channel, only 'when' and 'if'
		<-dbChan
	}
}

// don't touch below this line

func getDBsChannel(numDBs int) (chan struct{}, *int) {
	count := 0
	ch := make(chan struct{})

	go func() {
		for i := 0; i < numDBs; i++ {
			// the goroutine is blocked here until it is received in the `waitForDBs()` function
			// since the channel input happens `numDBs` # of times, the `waitForDBs()` function should receive a `numDBs` # of times as well
			// this stops the `count` from incrementing, which in turn causes the test-case to never exit the 'forever-loop' -> [main_test.go](line 28)
			ch <- struct{}{}
			fmt.Printf("Database %v is online\n", i+1)
			count++
		}
	}()

	// we want to return the `count` pointer because it is being incremented in another goroutine and we want the *latest* value of `count` 
	// (not the `count`) at the time of this function return
	return ch, &count
}

