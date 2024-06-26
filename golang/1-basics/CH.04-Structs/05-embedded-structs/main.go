// The difference between "Embedded" and "Nested" structs has to do with the level in which they are accessed.
// In Embedded structs, a struct grabs all the fields from another struct and treats them as top level fields (directly accessible from the struct)



package main

type sender struct {
	rateLimit int
	// this allows us to "inherit" the fields from the `user` struct
	// pretty much as close to "OOP Inheritence" as we are going to get
	user
}

type user struct {
	name   string
	number int
}

