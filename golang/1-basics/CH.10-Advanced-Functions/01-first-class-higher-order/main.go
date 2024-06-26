// Introduction to first class functions in GO
// We need to include the "function as a value's" type signature `func(string) string` in the function parameter



package main

func getFormattedMessages(messages []string, formatter func(string) string) []string {
	formattedMessages := []string{}
	for _, message := range messages {
		formattedMessages = append(formattedMessages, formatter(message))
	}
	return formattedMessages
}

