// This lesson is really just explaining the new lesson structure of testing our submitted code with unit-tests instead of console logging
// I made a cli function called `gotestboot` that will take in a dir to return the 'run' and 'submit' cases for the lesson



package main

func getMonthlyPrice(tier string) int {
	if tier == "basic" {
		return 10000
	}
	if tier == "premium" {
		return 15000
	}
	if tier == "enterprise" {
		return 50000
	}
	return 0
}

