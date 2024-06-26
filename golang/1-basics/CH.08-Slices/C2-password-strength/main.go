package main

func isValidPassword(password string) bool {
	//check if the password is greater than 5 and less than or equal to 12 characters long
	if len(password) < 5 || len(password) >= 12 {
		return false
	}

	hasUpper := false
	hasNumber := false
	for _, char := range password {
		// check against ASCII (uppercase alphabetic runes) {65 - 90}
		// 'A'(ascii) => 65 ; 'Z'(ascii) => 90
		if char >= 'A' && char <= 'Z' {
			hasUpper = true
		}
		// check against ASCII (numeric runes) {48 - 57}
		// '0'(ascii) => 48 ; '9'(ascii) => 57
		if char >= '0' && char <= '9' {
			hasNumber = true
		}
	}

	return hasUpper && hasNumber
}


// Below is an implementation without the knowledge of native ASCII integration in GO.


/*

// we set up our consts like this because when we iterate through the password below it will go over each character which is of type `rune`
const (
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numeric = "1234567890"
)

func isValidPassword(password string) bool {
	// check if the password is greater than 5 and less than or equal to 12 characters long
	if len(password) < 5 || len(password) >= 12 {
		return false
	}

	// our two conditions to be changed in order to pass
	a := false
	n := false
	for _, char := range password {
		for _, al := range alpha {
			// there needs to be at least one `char` that is an uppercase letter
			if char == al {
				a = true
			}
		}

		for _, nu := range numeric {
			// there needs to be at least one `char` that is a digit
			if char == nu {
				n = true
			}
		}
	}

	return a && n
}
*/
