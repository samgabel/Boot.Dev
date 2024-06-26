// This is explaining to us the nature of the loop statement: in this case running a forever loop



package main

func maxMessages(thresh int) int {
	var cost int

	// infinite loop until condition with return is hit
	for i := 0; ; i++ {
		cost += (100 + i)
		if cost > thresh {
			return i
		}
	}
}

