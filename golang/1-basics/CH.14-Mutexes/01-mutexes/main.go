// Shows us how mutexes are used to lock data from being accessed by multiple goroutines at the same time
// We use the "sync" standard package to import the `Mutex` struct tht provides our `Lock()` and `Unlock()`



package main

import (
	"sync"
	"time"
)

type safeCounter struct {
	counts map[string]int
	mu     *sync.Mutex
}

func (sc safeCounter) inc(key string) {
	// we first lock the struct
	// then we wait till the return to unlock it
	sc.mu.Lock()
	defer sc.mu.Unlock()

	sc.slowIncrement(key)
}

func (sc safeCounter) val(key string) int {
	// we first lock the struct
	// then we wait till the return to unlock it
	sc.mu.Lock()
	defer sc.mu.Unlock()

	return sc.slowVal(key)
}

// don't touch below this line

// the below simulates a multi-threaded environment (Maps are not thread-safe, need a mutex when accessing one -> in the presense of multiple goroutines)
// because GO code may or may not run on a single-core machine, it's best to write your code so that it's safe (no matter which hardware it runs on)

func (sc safeCounter) slowIncrement(key string) {
	tempCounter := sc.counts[key]
	time.Sleep(time.Microsecond)
	tempCounter++
	sc.counts[key] = tempCounter
}

func (sc safeCounter) slowVal(key string) int {
	time.Sleep(time.Microsecond)
	return sc.counts[key]
}

