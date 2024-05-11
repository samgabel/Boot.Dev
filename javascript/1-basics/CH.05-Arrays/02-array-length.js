// `length` is an array property, unlike the python `len()` function



/**
 * @param {string[]} usernames The array of usernames.
 * @returns {?string} The most recent username or null if the array is empty.
 */
const getMostRecentUser = (usernames) => {
    if (usernames.length === 0) {
        return null
    }
    return usernames[usernames.length - 1]
}


// don't touch below this line


console.log(`Most recent user: ${getMostRecentUser(
    []
)}`)

console.log(`Most recent user: ${getMostRecentUser(
    [
        'johndoe123',
        'billyrae456'
    ]
)}`)

console.log(`Most recent user: ${getMostRecentUser(
    [
        'wagslane',
        'jimmyjohn',
        'bopeep',
        'strightkilla',
        'reddyman'
    ]
)}`)

