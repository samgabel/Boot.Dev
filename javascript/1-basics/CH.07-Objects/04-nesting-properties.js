// We can also nest our properties and retrieve them like so



const review = {
    text: 'This movie was awful',
    stars: 2,
    author: {
        firstName: 'Johnny',
        lastName: 'Comelately',
        createdAt: '2022-08-17T15:41:25+00:00'
    }
}


// don't touch above this line


console.log(review.author.firstName)

