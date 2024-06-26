package main

import "strings"

func countDistinctWords(messages []string) int {
	// create a hashmap in order to find the unique words
	countMap := make(map[string]int)
	for _, msg := range messages {
		// this will take each message string and split them into a slice of individual words (by presense of unicode space character)
		words := strings.Fields(msg)

		// now iterate over the words in each msg, normalize the word (lowercase), and add them to the hashmap
		for _, word := range words {
			wordLower := strings.ToLower(word)
			countMap[wordLower]++
		}
	}

	return len(countMap)
}

