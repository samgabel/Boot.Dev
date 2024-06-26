package main

func findSuggestedFriends(username string, friendships map[string][]string) []string {
	// create a map of direct friends
	directFriends := make(map[string]bool)
	for _, friend := range friendships[username] {
		directFriends[friend] = true
	}

	// create a map of all indirect freinds (friend of friend) -> discluding the `username` and direct friends
	indirectFriends := make(map[string]bool)
	for _, friend := range friendships[username] {
		for _, indirectFriend := range friendships[friend] {
			// we essentially created the directFriends hashmap so we could check this
			if indirectFriend != username && !directFriends[indirectFriend] {
				indirectFriends[indirectFriend] = true
			}
		}
	}

	// append the map keys to a slice that will be returned
	var suggestedFriends []string
	for mutualFriend := range indirectFriends {
		suggestedFriends = append(suggestedFriends, mutualFriend)
	}

	return suggestedFriends
}

