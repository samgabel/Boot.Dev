// Similar to python's `None` value, JavaScript has a `null` value that can be used as a "default"

// `null` values are falsey
// Falsey -> false , ''     , 0
// Truthy -> true  , 'name' , 1



const movieTitle = null

// don't touch below this line

// The 'not' operator implicitly
// casts movieTitle to a boolean value
const movieHasNoTitle = !movieTitle

console.log(`The movie does not have a title: ${movieHasNoTitle}`)
