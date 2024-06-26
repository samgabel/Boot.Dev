// Any struct with a method called `Error()` implements the error interface.



package main

import (
	"fmt"
)

type divideError struct {
	dividend float64
}

// This method `Error()` of the divideError struct implements the `error` interface
func (d divideError) Error() string {
	return fmt.Sprintf("can not divide %v by zero", d.dividend)
}

// One of our return values is a `error` type because we return divideError() which itself implements the error interface
func divide(dividend, divisor float64) (float64, error) {
	if divisor == 0 {
		return 0, divideError{dividend: dividend}
	}
	// We either return an error or `nil` if the function executes properly
	return dividend / divisor, nil
}

