// We can nest structs to inherit the `fields` of the referenced struct
// For example the `messageToSend.sender` field is of type `user` which is a struct that has `name` and `number` fields.



package main

type messageToSend struct {
	message   string
	sender    user
	recipient user
}

type user struct {
	name   string
	number int
}

func canSendMessage(mToSend messageToSend) bool {
	sender := mToSend.sender
	recipient := mToSend.recipient

	if sender.name == "" || sender.number == 0 {
		return false
	}
	if recipient.name == "" || recipient.number == 0 {
		return false
	}
	return true
}

