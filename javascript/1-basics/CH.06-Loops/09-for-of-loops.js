// `of` keyword functions the same as the `in` keyword in python
// Use this when we want to iterate through the entire iterable in ascending order / we do NOT need the index or to modify the array's items



/**
 * @param {string[]} reviews
 * @param {string} badWord
 */
const printCleanReviews = (reviews, badWord) => {
    for (let review of reviews) {
        if (review.includes(badWord)) {
            continue
        }
        console.log(`Clean review: ${review}`)
    }
}

// don't touch below this line

printCleanReviews(['The movie sucks', 'I love it', 'What garbage', 'so sucky'], 'suck')
console.log('---')
printCleanReviews(['The movie sucks', 'I love it', 'What darn crap', 'darn, so sucky'], 'darn')
console.log('---')

