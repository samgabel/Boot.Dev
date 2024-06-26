// The grand majority of the time in GO we will use slices instead of arrays, because of their mutable and flexible nature
// A slice is a dynamically sized, flexible view of the elements of an array



package main

import "errors"

const (
	planFree = "free"
	planPro  = "pro"
)

func getMessageWithRetriesForPlan(plan string, messages [3]string) ([]string, error) {
	if plan == planPro {
		return messages[:], nil
	}

	if plan == planFree {
		return messages[:2], nil
	}

	return nil, errors.New("unsupported plan")
}

