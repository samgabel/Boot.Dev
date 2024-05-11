// Two different ways to concatenate arrays...
// using `concat` method (note: this creates a new array of the concatenated arrays, it does NOT modify the original array in place)
// using "spread" syntax ( [...array, ...array, string, string] )

// Because of `concat` creating a new array, using "spread" syntax is more intuitive



/**
 * @param {string[]} oldMovies
 * @param {string[]} newMovies
 * @returns {string[]} The combination of `oldMovies` and `newMovies`
 */
const uploadNewMovies = (oldMovies, newMovies) => {
    // `concat` method
    // return oldMovies.concat(newMovies)

    // spread syntax
    return [...oldMovies, ...newMovies]
}


// don't touch below this line


const oldMovies = ['Once Upon a Time', 'Django Unchained', 'The Hateful 8']
const newMovies = ['Inglorious Basterds', 'Dune']
const allMovies = uploadNewMovies(oldMovies, newMovies)

console.log('All movies database:')
logArray(allMovies)


function logArray(arr) {
    for (const a of arr) {
        console.log(` - ${a}`)
    }
    console.log('---')
}

