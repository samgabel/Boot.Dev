// This shows that we can have a type implement more than one interface



package main

import "fmt"

func (e email) cost() int {
	if !e.isSubscribed {
		return len(e.body) * 5
	}
	return len(e.body) * 2
}

func (e email) format() string {
	subscriptionStatus := "Not Subscribed"
	if e.isSubscribed {
		subscriptionStatus = "Subscribed"
	}

	return fmt.Sprintf("'%s' | %s", e.body, subscriptionStatus)
}

type expense interface {
	cost() int
}

type formatter interface {
	format() string
}

type email struct {
	isSubscribed bool
	body         string
}

