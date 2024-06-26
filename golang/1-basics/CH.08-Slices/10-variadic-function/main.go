// We can take in a variable number of arguments into a function using the spread `...` operator
// These arguments pass in the arguments into the function as a SLICE



package main

func sum(nums ...int) int {
	var sum int

	for _, num := range nums {
		sum += num
	}

	return sum
}

