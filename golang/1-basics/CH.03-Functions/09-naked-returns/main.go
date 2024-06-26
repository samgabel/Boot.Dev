// We can explicitly declare which variables (and their types) we wan't to return in the function declaration
// This allows us to have a "clean" return statement, where we just type `return`

// We should probably only used this "naked" return in small functions, for larger/complex functions, "named" returns would be better



package main

func yearsUntilEvents(age int) (yearsUntilAdult, yearsUntilDrinking, yearsUntilCarRental int) {
	yearsUntilAdult = 18 - age
	if yearsUntilAdult < 0 {
		yearsUntilAdult = 0
	}
	yearsUntilDrinking = 21 - age
	if yearsUntilDrinking < 0 {
		yearsUntilDrinking = 0
	}
	yearsUntilCarRental = 25 - age
	if yearsUntilCarRental < 0 {
		yearsUntilCarRental = 0
	}
	// this is considered a naked return (only use for simple/small functions)
	return
}

