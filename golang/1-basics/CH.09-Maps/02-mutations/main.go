// This is showing us how we can grab and mutate the state of a map in GO



package main

import "errors"

func deleteIfNecessary(users map[string]user, name string) (deleted bool, err error) {
	// grabbing value (user struct) and checking if it exists
	elem, ok := users[name]

	// user doesn't exist in the map
	if !ok {
		return false, errors.New("not found")
	}

	// user isn't scheduled for deletion
	if !elem.scheduledForDeletion {
		return false, nil
	}

	// all cases pass
	delete(users, name)
	return true, nil
}

type user struct {
	name                 string
	number               int
	scheduledForDeletion bool
}

