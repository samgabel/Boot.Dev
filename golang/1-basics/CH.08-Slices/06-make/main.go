// Initializing a new empty slice with built-in `make()` function



package main

func getMessageCosts(messages []string) []float64 {
	length := len(messages)
	messageCosts := make([]float64, length)

	for i := 0; i < length; i++ {
		messageCosts[i] = float64(len(messages[i])) * 0.01
	}

	return messageCosts
}

