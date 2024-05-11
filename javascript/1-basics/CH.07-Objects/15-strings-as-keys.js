// We can use the bracket notation to create or modify a key (exactly like in Python)
// This allows us to use *strings* as keys instead of having to manually code a new key (ie: movies['title'] instead of movies.title)



/**
 * @param {string[]} movies
 * @returns {object} An object with movie titles as keys and counts as values
 */
const getCountsByTitle = (movies) => {
    const count = {}
    for (let title of movies) {
        if (!count[title]) {
            count[title] = 0
        }
        count[title]++
    }
    return count
}

// don't touch below this line

function test(movies) {
    const counts = getCountsByTitle(movies)
    for (const [movie, count] of Object.entries(counts)) {
        console.log(`'${movie}' has ${count} reviews`)
    }
    console.log('---')
}

test([
    'Ice Age',
    'The Forgotten',
    'The Northman',
    'American Psycho',
    'Ice Age',
    'Ice Age',
    'American Psycho'
])

test([
    'Big Daddy',
    'Big Daddy',
    'The Big Short',
    'The Big Short',
    'The Big Short'
])

