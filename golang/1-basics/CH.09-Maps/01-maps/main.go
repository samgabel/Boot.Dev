// We either us the `make()` function or use the map literal mapObject = map[string]int{}



package main

import "errors"

func getUserMap(names []string, phoneNumbers []int) (map[string]user, error) {
	// check if there is an inequality between key->value pairs first
	if len(names) != len(phoneNumbers) {
		return nil, errors.New("invalid sizes")
	}

	// use the `make()` built-in function to initialize a map
	userMap := map[string]user{}
	for i := 0; i < len(names); i++ {
		userMap[names[i]] = user{name: names[i], phoneNumber: phoneNumbers[i]}
	}

	return userMap, nil
}

type user struct {
	name        string
	phoneNumber int
}

