// Here we delve into the `Promise` object which we use in conjunction with `then/catch`
// This allows us to specify and action/message for a successful/failed Promise object



const applyDamage = (damage, currentHP) => {
    // return a new `Promise` object that takes in 2 callbacks (resolve and reject)
    return new Promise((resolve, reject) => {
        // set up an async function and a "passing"(resolve) condition and a "failing"(reject) condition
        setTimeout(() => {
            if (currentHP <= damage) {
                reject(`The player suffers ${damage} points of damage and has fallen unconscious.`)
            } else {
                resolve(`The player suffers ${damage} points of damage and has ${currentHP - damage} hit points remaining.`)
            }
        }, 300)
    })
}


// Don't touch below this line


function runApplyDamageTest(damage, currentHP) {
    console.log(`Applying ${damage} damage to player with ${currentHP} HP...`)
    // when we call the function that contains the Promise, we then have a `then/catch` block to log resolve/reject
    applyDamage(damage, currentHP)
        .then(message => console.log(`...applyDamage resolved with: ${message}`))
        .catch(message => console.log(`...applyDamage rejected with: ${message}`))
}

runApplyDamageTest(27, 50)
await sleep(400)
runApplyDamageTest(50, 50)
await sleep(400)
runApplyDamageTest(110, 100)
await sleep(400)

function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms))
}
