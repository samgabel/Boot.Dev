// Arrays in GO are statically typed and fixed-sized



package main

func getMessageWithRetries(primary, secondary, tertiary string) ([3]string, [3]int) {
	// messages array
	messages := [3]string{
		primary,
		secondary,
		tertiary,
	}

	// costs array
	costs := [3]int{
		len(primary),
		len(primary) + len(secondary),
		len(primary) + len(secondary) + len(tertiary),
	}

	return messages, costs
}
