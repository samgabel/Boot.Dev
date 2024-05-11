// `continue` will skip the loop current iteration and go to the next iteration



/**
 * @param {string[]} reviews
 * @param {string} badWord
 */
const printCleanReviews = (reviews, badWord) => {
    for (i = 0; i < reviews.length; i++) {
        // don't print review if it contains the `badWord`
        if (reviews[i].includes(badWord)) {
            continue
        }
        console.log(`Clean review: ${reviews[i]}`)
    }
}


// don't touch below this line


printCleanReviews(['The movie sucks', 'I love it', 'What garbage', 'so sucky'], 'suck')
console.log('---')
printCleanReviews(['The movie sucks', 'I love it', 'What darn crap', 'darn, so sucky'], 'darn')
console.log('---')

