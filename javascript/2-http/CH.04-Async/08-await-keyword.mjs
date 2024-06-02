// This is supposed to show us that we can just use the `await` keyword which is a lot cleaner looking a less granular than `then/catch`



const message = await applyDamage(25, 50)

// Don't touch below this line

console.log(message)

function applyDamage(damage, currentHP) {
    return new Promise((resolve) => {
        const newHP = currentHP - damage
        setTimeout(() => {
            resolve(`The player with ${currentHP} hit points suffers ${damage} points of damage and has ${newHP} hit points remaining.`)
        }, 1000)
    })
}
