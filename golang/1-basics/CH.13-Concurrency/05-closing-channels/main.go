// This is supposed to show us that we can close channels
// closing a channel is not really required because an unused open channel will eventually be garbage collected



package main

func countReports(numSentCh chan int) int {
	count := 0

	for true {
		// ok is a boolean where `true` is an open channel and `false` is a closed channel
		v, ok := <-numSentCh
		if !ok {
			break
		}

		// increment our return value by the number of reports per 'batch'
		count += v
	}

	return count
}

// don't touch below this line

func sendReports(numBatches int, ch chan int) {
	for i := 0; i < numBatches; i++ {
		numReports := i*23 + 32%17
		ch <- numReports
	}
	close(ch)
}

