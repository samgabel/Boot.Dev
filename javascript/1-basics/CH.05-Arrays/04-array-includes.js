// `includes` array method will return a boolean based off of if a string is present in the array
// * also serves as a string method and will return a boolean based off if a certain sequence of characters is in the string



/**
 * @param {string[]} reviewWords
 * @returns {string} The ranking of profanity
 */
function getCleanRank(reviewWords) {
    let numWords = 0
    if (reviewWords.includes('dang')) {
        numWords++
    }
    if (reviewWords.includes('shoot')) {
        numWords++
    }
    if (reviewWords.includes('heck')) {
        numWords++
    }

    // return string based on count of bad words
    if (numWords === 0) {
        return 'clean'
    } else if (numWords === 1) {
        return 'dirty'
    } else {
        return 'filthy'
    }
}


// Don't edit below this line


function test(reviewWords) {
    const cleanRank = getCleanRank(reviewWords)
    console.log(`'${reviewWords}' has rank: ${cleanRank}`)
}

test(['avril', 'lavigne', 'has', 'best', 'dang', 'tour'])
test(['what', 'a', 'bad', 'film'])
test(['oh', 'my', 'heck', 'I', 'hated', 'it'])
test(['ripoff'])
test(['That', 'was', 'a', 'pleasure'])
test(['shoot!', 'I', 'cant', 'say', 'I', 'liked', 'the', 'dang', 'thing'])
test(['shoot', 'dang', 'heck'])

