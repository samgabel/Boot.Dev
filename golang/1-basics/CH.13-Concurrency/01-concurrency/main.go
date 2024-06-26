// This shows us that we can specify that we want a function to fun concurrently using the `go` keyword



package main

import (
	"fmt"
	"time"
)

func sendEmail(message string) {
	// we use the `go` keyword to specify this code running in a seperate 'goroutine'
	go func() {
		time.Sleep(time.Millisecond * 250)
		fmt.Printf("Email received: '%s'\n", message)
	}()
	fmt.Printf("Email sent: '%s'\n", message)
}

// Don't touch below this line

func test(message string) {
	sendEmail(message)
	time.Sleep(time.Millisecond * 500)
	fmt.Println("========================")
}

func main() {
	test("Hello there Kaladin!")
	test("Hi there Shallan!")
	test("Hey there Dalinar!")
}

