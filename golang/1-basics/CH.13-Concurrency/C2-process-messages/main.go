package main

func processMessages(messages []string) []string {
	processedMessages := []string{}
	messageChan := make(chan string, len(messages))

	for _, message := range messages {
		go func(m string) {
			m += "-processed"
			messageChan <- m
		}(message)

		processedMessages = append(processedMessages, <-messageChan)
	}

	return processedMessages
}

