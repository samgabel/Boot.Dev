// We can use the `range` keyword to iterate over a channel, so long as that channel is eventually closed



package main

func concurrentFib(n int) []int {
	ch := make(chan int)

	// call the `fibonacci()` function concurrently
	go fibonacci(n, ch)

	// range over the `num` received from the channel
	// blocking at each iteration if nothing new is there
	// will exit once the channel is closed
	fibNums := []int{}
	for num := range ch {
		fibNums = append(fibNums, num)
	}

	return fibNums
}

// don't touch below this line

func fibonacci(n int, ch chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		ch <- x
		x, y = y, x+y
	}
	close(ch)
}

