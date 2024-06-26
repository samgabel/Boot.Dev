package main

import (
	"fmt"
)

func printPrimes(max int) {
OuterLoop:
	for n := 2; n < max+1; n++ {
		// 2 is prime
		if n == 2 {
			fmt.Println(n)
			continue
		}

		// if n is even it is not prime
		if n%2 == 0 {
			continue
		}

		// if an odd number (i) up to the sqrt(n) is a factor of n, then it is not prime
		for i := 3; i*i <= n; i += 2 {
			if n%i == 0 {
				continue OuterLoop
			}
		}

		// if all guard clauses pass then we have ourselves a prime number
		fmt.Println(n)
	}
}

// don't edit below this line

func test(max int) {
	fmt.Printf("Primes up to %v:\n", max)
	printPrimes(max)
	fmt.Println("===============================================================")
}

func main() {
	test(10)
	test(20)
	test(30)
}
