// This is definitely not what you want to do when trying to make an asynchronous component, but this demonstrates what being asynchronous means

// Since `setTimeout` is an async function, that means that the timer function will not pause the execution of other components in the functions stack



const craftingCompleteWait = 400
const combiningMaterialsWait = 200
const smeltingIronBarsWait = 100
const shapingIronWait = 300


// Don't touch below this line


setTimeout(() => console.log('Iron Longsword Complete!'), craftingCompleteWait)
setTimeout(() => console.log('Combining Materials...'), combiningMaterialsWait)
setTimeout(() => console.log('Smelting Iron Bars...'), smeltingIronBarsWait)
setTimeout(() => console.log('Shaping Iron...'), shapingIronWait)

console.log('Firing up the forge...')

await sleep(500)
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms))
}
