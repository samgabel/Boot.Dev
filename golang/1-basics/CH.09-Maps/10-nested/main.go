package main

func getNameCounts(names []string) map[rune]map[string]int {
	// initialize return map
	returnMap := make(map[rune]map[string]int)
	// iterate over `names` slice
	for _, name := range names {

		// `rune` (int32) cover "multi-byte" Unicode characters (U+0000) // `byte` (uint8) cover ASCII (0-127)
		// we set each name to be split by each character (type cast) into a slice of runes
		characterRunes := []rune(name)
		firstLetter := characterRunes[0]

		// first layer
		if _, ok := returnMap[firstLetter]; !ok {
			returnMap[firstLetter] = make(map[string]int)
		}

		// second layer
		if _, ok := returnMap[firstLetter][name]; !ok {
			returnMap[firstLetter][name] = 0
		}

		returnMap[firstLetter][name]++
	}

	return returnMap
}

