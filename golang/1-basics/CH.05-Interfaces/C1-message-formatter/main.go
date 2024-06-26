package main

import "fmt"

type Formatter interface {
	Format() string
}

// PLAINTEXT
type PlainText struct {
	message string
}
func (p PlainText) Format() string {
	return p.message
}

// BOLD
type Bold struct {
	message string
}
func (b Bold) Format() string {
	return fmt.Sprintf("**%s**", b.message)
}

// CODE
type Code struct {
	message string
}
func (c Code) Format() string {
	return fmt.Sprintf("`%s`", c.message)
}

// Don't Touch below this line

func SendMessage(formatter Formatter) string {
	return formatter.Format() // Adjusted to call Format without an argument
}

