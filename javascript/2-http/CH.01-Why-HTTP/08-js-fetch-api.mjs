// This shows in more depth how the `fetch()` function works



const apiKey = generateKey()
const url = getURL()
const settings = getSettings()

// we need to wait for the contents of the return of the `fetch()` function (the return is a promise so we use `await`)
const response = await fetch(url, settings)
// the return of the `json()` method (which converts the server response data into a JavaScript object) is also a promise so we use `await`
const responseData = await response.json()

logItems(responseData)


// don't touch below this line


function getSettings() {
    return {
        method: 'GET',
        mode: 'cors',
        headers: {
            'X-API-Key': apiKey,
            'Content-Type': 'application/json'
        }
    }
}

function getURL() {
    return 'https://api.boot.dev/v1/courses_rest_api/learn-http/items'
}

function generateKey() {
    const characters = 'ABCDEF0123456789'
    let result = ''
    for (let i = 0; i < 16; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length))
    }
    return result
}

function logItems(items) {
    for (const item of items) {
        console.log(item.name)
    }
}
