package main

func calculateFinalBill(costPerMessage float64, numMessages int) float64 {
	return costPerMessage * float64(numMessages) * calculateDiscount(numMessages)
}

func calculateDiscount(messagesSent int) float64 {
	if messagesSent > 5000 {
		return 0.80
	}
	if messagesSent > 1000 {
		return 0.90
	}
	return 1.00
}

// don't touch below this line

func calculateBaseBill(costPerMessage float64, messagesSent int) float64 {
	return costPerMessage * float64(messagesSent)
}
