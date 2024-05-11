// Essentially a JavaScript Object type is a variable that can hold custom properties.
// Works kind of like a Python dictionary where we can identify a key (property) and associated value (property value)



/**
 * @param {string} title
 * @param {number} stars
 * @param {string} username
 * @returns {object} An object with `title`, `stars`, `username`, and `id` properties
 */
function getMovieRecord(title, stars, username) {
    const record = {
        // title: title,
        title,
        // stars: stars,
        stars,
        // username: username,
        username,
        id: `${title}-${username}`
    }
    return record
}


// Don't touch below this line


logObject(getMovieRecord('oh brother where art thou', 3, 'wagslane'))
logObject(getMovieRecord('frozen', 5.5, 'elonmusk'))
logObject(getMovieRecord('toy story', 4, 'prince'))

function logObject(obj) {
    for (const key in obj) {
        console.log(` - ${key}: ${obj[key]}`)
    }
    console.log('---')
}
