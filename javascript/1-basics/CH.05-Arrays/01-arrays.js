// Arrays function almost identically to lists in Python

// notice how we use `const` but can still `push` to the array ...
// because we aren't reassigning `movies` to a new value or array, just updating whats inside
// `push` is synonomous with the python `append`



const movies = []
movies.push('the dark knight')
logArray(movies)
movies.push('the notebook')
logArray(movies)
console.log(movies[0])

// don't touch below this line

function logArray(arr) {
    console.log('logging array...')
    for (const a of arr) {
        console.log(` - ${a}`)
    }
    console.log('---')
}

