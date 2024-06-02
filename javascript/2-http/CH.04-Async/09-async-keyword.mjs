// We can only use the `await` keyword in the top-level of modules or in `async` functions
// If you think about it, we need to pause code execution at the `await` keyword, so the function encapsulating it needs to be asynchronous



const items = await getItemData()
logItems(items)

// running this code without the `async` keyword in front of this function containing `await` gives us an error
async function getItemData() {
    const response = await fetch('https://api.boot.dev/v1/courses_rest_api/learn-http/items', getSettings())
    return response.json()
}


// same thing but with .then() instead of async/await


// getItemData()
//     // when `getItemData()` resolves, we take the return (items) and execute the callback within `.then()`
//     .then(items => logItems(items));
//
// function getItemData() {
//     return fetch('https://api.boot.dev/v1/courses_rest_api/learn-http/items')
//         // when `fetch()` resolves, we take the return (response) and execute the callback within `.then()`
//         .then(response => response.json());
// }


// don't touch below this line


function getSettings() {
    return {
        method: 'GET',
        mode: 'cors',
        headers: {
            'X-API-Key': 'Testing',
            'Content-Type': 'application/json'
        }
    }
}

async function logItems(items) {
    for (const item of items) {
        console.log(item.quality, item.name)
        await sleep(44)
    }
}

function sleep(ms) {
    // we construct a new `Promise` object and pass a resolve callback (and optionally a reject callback) to the "executor function"
    // within the "executor function" we call setTimeout to run the resolve callback once the parameter of our `sleep()` function `ms` is called
    // * remember, for these functions that take callbacks as arguments, we want to pass the callback object itself, not the return of the callback
    // * `resolve` not `resolve('...')`, if we want to pass a value to the `resolve` callback we do `setTimeout(() => resolve('...'), ms)`
    return new Promise(resolve => setTimeout(resolve, ms))
}
