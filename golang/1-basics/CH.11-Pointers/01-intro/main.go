// This was supposed to show us that printing the actual pointer (&variable) shows the location in memory



package main

import "fmt"

type Message struct {
	Recipient string
	Text      string
}

func getMessageText(m Message) string {
	return fmt.Sprintf(`
To: %v
Message: %v
`, m.Recipient, m.Text)
	// was &m.Recipient, &m.Text
	// this prints to console what the memory address location is not the actual value
}

