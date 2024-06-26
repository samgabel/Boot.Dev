package main

import "strings"

type sms struct {
	id      string
	content string
	tags    []string
}

func tagMessages(messages []sms, tagger func(sms) []string) []sms {
	for i, msg := range messages {
		messages[i].tags = tagger(msg)
	}

	return messages
}

func tagger(msg sms) []string {
	tags := []string{}

	if strings.Contains(msg.content, "Urgent") || strings.Contains(msg.content, "urgent") {
		tags = append(tags, "Urgent")
	}
	if strings.Contains(msg.content, "Sale") || strings.Contains(msg.content, "sale") {
		tags = append(tags, "Promo")
	}

	return tags
}
