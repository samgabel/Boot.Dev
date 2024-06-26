package main

func getPacketSize(message string) int {
	messageLen := len(message)

	// if `messageLen` is prime then the packet size can only be prime as well
	if isPrime(messageLen) {
		return 0
	}

	for i := messageLen; i > 1; i-- {
		// if `i` is a factor of messageLen
		if messageLen % i == 0 {
			// and the # of packets (`messageLen / i`) is not prime
			if !isPrime(messageLen / i) {
				// return the largest packet size (`i`)
				return i
			}
		}
	}

	return 0
}

func isPrime(num int) bool {
	if num == 2 {
		return true
	}

	if num%2 == 0 {
		return false
	}

	for i := 3; i*i <= num; i += 2 {
		if num%i == 0 {
			return false
		}
	}
	return true
}

