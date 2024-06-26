// This explains to us the power of the RWMutex, we can have simultaneous read locks (blocking only write Lock() operations)
// it's useful when we have many sources that want to read from the same data at the same time



package main

import (
	"sync"
	"time"
)

type safeCounter struct {
	counts map[string]int
	mu     *sync.RWMutex
}

func (sc safeCounter) inc(key string) {
	sc.mu.Lock()
	defer sc.mu.Unlock()
	sc.slowIncrement(key)
}

func (sc safeCounter) val(key string) int {
	// we can have multiple goroutines utilizing RLock() (multiple simultaneous read operations, excluding write operations),
	// only one goroutine can utilize Lock(), all other RLock()'s will be excluded (1 write lock, no reads or writes during that lock)
	sc.mu.RLock()
	defer sc.mu.RUnlock()
	return sc.counts[key]
}

// don't touch below this line

func (sc safeCounter) slowIncrement(key string) {
	tempCounter := sc.counts[key]
	time.Sleep(time.Microsecond)
	tempCounter++
	sc.counts[key] = tempCounter
}

