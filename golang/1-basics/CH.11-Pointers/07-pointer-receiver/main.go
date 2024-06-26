// A Pointer Receiver is the most common way to implement a method (value receivers are less common)
// Think of this as a way for the method to mutate the instance of the struct rather than the struct type itself



package main

// we want to use a pointer receiver to modify the specific instance of the struct being passed to this method
func (e *email) setMessage(newMessage string) {
	e.message = newMessage
}

// don't edit below this line

type email struct {
	message     string
	fromAddress string
	toAddress   string
}

