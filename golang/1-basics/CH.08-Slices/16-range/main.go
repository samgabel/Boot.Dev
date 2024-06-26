// The `range` keyword iterates over each element of a slice or array and returns the current index and the element itself (in that order).



package main

func indexOfFirstBadWord(msg []string, badWords []string) int {
	for i, word := range msg {
		for _, badWord := range badWords {
			if word == badWord {
				return i
			}
		}
	}

	return -1
}

