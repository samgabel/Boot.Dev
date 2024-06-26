// One thing to REALLY note is that it is good practice to properly initialize structs:
// Even though the `Membership` struct is imbedded in the `User` struct we should seek to initialize the `Membership` separately



package main

type membershipType string

const (
	TypeStandard membershipType = "standard"
	TypePremium  membershipType = "premium"
)

// don't touch above this line

type User struct {
	Name string
	// User embeds Membership struct
	Membership
}

type Membership struct {
	Type             membershipType
	MessageCharLimit int
}

func newUser(name string, membershipType membershipType) User {
	// initialize Membership struct
	membership := Membership{Type: membershipType}

	// find messageCharLimit
	if membershipType == TypePremium {
		membership.MessageCharLimit = 1000
	} else {
		membership.MessageCharLimit = 100
	}

	// return User struct with values
	return User{Name: name, Membership: membership}
}
