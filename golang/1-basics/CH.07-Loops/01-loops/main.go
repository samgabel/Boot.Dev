package main

func bulkSend(numMessages int) float64 {
	var cost float64

	for i := 0; i < numMessages; i++ {
		cost += 1 + (float64(i) * 0.01)
	}

	return cost
}
