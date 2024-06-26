// This shows us that buffered channels are meant for batches of data...

// Sending on a buffered channel only blocks when the buffer is full
// Receiving blocks only when the buffer is empty



package main

func addEmailsToQueue(emails []string) chan string {
	// create our buffered channel
	ch := make(chan string, len(emails))

	for _, email := range emails {
		ch <- email
	}

	return ch
}

