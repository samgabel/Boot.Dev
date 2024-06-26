// Shows us how we dereference pointers in order to get and mutate variable values



package main

import (
	"strings"
)

func removeProfanity(message *string) {
	badWords := []string{"fubb", "shiz", "witch"}
	for _, word := range badWords {
		// dereference the `message` pointer in order to update the value at the memory register
		*message = strings.ReplaceAll(*message, word, strings.Repeat("*", len(word)))
	}
}

