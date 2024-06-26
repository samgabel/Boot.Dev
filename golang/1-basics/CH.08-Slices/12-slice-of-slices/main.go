// This lesson teaches us about slice of slices (matrix or 2d grid)



package main

func createMatrix(rows, cols int) [][]int {
	// we probably should use the `make()` function because it preallocated memory instead of having to dynamically reassign the slice each iteration
	matrix := make([][]int, rows)
	for i := 0; i < rows; i++ {

		// still need to create the array for each row (again using `make()` to preallocated memory to the creation of the slice)
		matrix[i] = make([]int, cols)
		for j := 0; j < cols; j++ {

			// here we set the grid value to the product of the indices of the current row & col
			matrix[i][j] = i * j
		}
	}

	return matrix
}

