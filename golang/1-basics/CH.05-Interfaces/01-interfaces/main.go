// I talk about how GO interfaces are used with structs and methods and how it resembles Polymorphism (read commments for more explanantion)



package main

import (
	"fmt"
	"time"
)

// The `getMessage()` method is called on `msg`, which can be any type
// that implements the `message` interface (either `birthdayMessage` or `sendingReport`).
func sendMessage(msg message) (string, int) {
	m := msg.getMessage()
	return m, len(m) * 3
}

// The `message` interface is an example of Go polymorphism.
// It allows the `getMessage()` method to be common across different types (like `birthdayMessage` and `sendingReport`),
// but the behavior of `getMessage()` differs depending on the calling object.
type message interface {
	getMessage() string
}

// don't edit below this line

type birthdayMessage struct {
	birthdayTime  time.Time
	recipientName string
}

func (bm birthdayMessage) getMessage() string {
	return fmt.Sprintf("Hi %s, it is your birthday on %s", bm.recipientName, bm.birthdayTime.Format(time.RFC3339))
}

type sendingReport struct {
	reportName    string
	numberOfSends int
}

func (sr sendingReport) getMessage() string {
	return fmt.Sprintf(`Your "%s" report is ready. You've sent %v messages.`, sr.reportName, sr.numberOfSends)
}

