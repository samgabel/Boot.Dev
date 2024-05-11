// `var` is a legacy keyword that really shouldn't be used, it allows you to break out of block scopes (ie: if/else blocks)



function getIsPowerUser(numReviews) {
    // if (numReviews > 10) {
    //     var isPowerUser = true
    // }
    // return isPowerUser

    // instead lets just do this
    return numReviews > 10
}

// don't touch below this line

function test(numReviews) {
    const isPowerUser = getIsPowerUser(numReviews)
    console.log(`Number of reviews: ${numReviews}, is power user: ${isPowerUser}`)
}

test(100)
test(50)
test(10)
test(5)
test(2)

