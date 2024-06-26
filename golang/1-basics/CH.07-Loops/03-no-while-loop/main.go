// There are no `while` loops in GO so we use the for loop with only a CONDITION in the statement.



package main

func getMaxMessagesToSend(costMultiplier float64, maxCostInPennies int) int {
	actualCostInPennies := 1.0
	maxMessagesToSend := 1

	// We can also just specify a CONDITION as the only statement to basically transform a for loop into a while loop
	for actualCostInPennies < float64(maxCostInPennies) {
		actualCostInPennies *= costMultiplier
		maxMessagesToSend++
	}

	if actualCostInPennies > float64(maxCostInPennies) {
		maxMessagesToSend--
	}

	return maxMessagesToSend
}

