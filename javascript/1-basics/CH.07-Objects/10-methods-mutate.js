// We create an Object method that will modify some property.
// When this Object method is called, it will serve to mutate the object.



const author = {
    name: 'Simon Garfunkle',
    numReviews: 8,
    // increments `numReviews` propery by 1 when the method is called
    submitReview() {
        this.numReviews++
    }
}


// don't touch below this line


console.log(`${author.name} has submitted ${author.numReviews} reviews`)

console.log(`${author.name} is submitting a review...`)
author.submitReview()
console.log(`${author.name} has submitted ${author.numReviews} reviews`)

console.log(`${author.name} is submitting a review...`)
author.submitReview()
console.log(`${author.name} has submitted ${author.numReviews} reviews`)

console.log(`${author.name} is submitting a review...`)
author.submitReview()
console.log(`${author.name} has submitted ${author.numReviews} reviews`)

console.log(`${author.name} is submitting a review...`)
author.submitReview()
console.log(`${author.name} has submitted ${author.numReviews} reviews`)

