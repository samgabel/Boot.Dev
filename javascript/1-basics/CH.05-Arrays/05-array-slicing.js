// While the built-in array syntax does not allow negative indexing, the `slice` method DOES allow negative indexing



const movies = [
    'oh brother where art thou',
    'oceans eleven',
    'fight club',
    'the island',
    'shutter island',
    'the magnificent seven'
]

function logArray(arr) {
    for (const a of arr) {
        console.log(` - ${a}`)
    }
    console.log('---')
}


// don't touch above this line


// 3rd -> last
logArray(movies.slice(2))
// 1st -> 3rd to last
logArray(movies.slice(0, -2))

