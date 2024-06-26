// Generics allow us to repeat functionality for a variety of compatible types
// Essentially we use a variable `T` in order to refer to certain types (in this case we use `T` to refer to `any` type)



package main

func getLast[T any](s []T) T {
	if len(s) == 0 {
		// get the zeroValue value of T
		var zeroValue T
		// return the specific zero value of the empty slice
		return zeroValue
	}

	// return the last value in the slice
	return s[len(s) - 1]
}

