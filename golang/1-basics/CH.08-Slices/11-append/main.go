// The `append()` built-in function will return a new slice where we specify the underlying slice/array and then the value we want to "append"



package main

type cost struct {
	day   int
	value float64
}

func getCostsByDay(costs []cost) []float64 {
	costByDay := []float64{}

	// iteratre over all the costs
	for i := 0; i < len(costs); i++ {
		cost := costs[i]

		// if the current iteration of costs is a day specified that is larger than the list we are returning...
		// append empty costs for each of those intermediary days
		for cost.day >= len(costByDay) {
			costByDay = append(costByDay, 0.0)
		}

		// finally update the cost of that current iteration with the value
		costByDay[cost.day] += cost.value
	}

	return costByDay
}
