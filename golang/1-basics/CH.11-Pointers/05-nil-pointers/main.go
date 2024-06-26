// Pointers in GO are dangerous because we will get a runtime (panic) error if we attempt to dereference a nil pointer



package main

import (
	"strings"
)

func removeProfanity(message *string) {
	// i feel like this is stupid, there should be a bool err return from dereferencing a pointer
	if message == nil {
		return
	}
	// if you try to dereference a nil pointer it will cause a runtime error (a panic) that crashes the program
	messageVal := *message
	messageVal = strings.ReplaceAll(messageVal, "fubb", "****")
	messageVal = strings.ReplaceAll(messageVal, "shiz", "****")
	messageVal = strings.ReplaceAll(messageVal, "witch", "*****")
	*message = messageVal
}

