// This is supposed to show use how the `.json()` method of the `Response` object works



async function getLocations() {
    const url = 'https://api.boot.dev/v1/courses_rest_api/learn-http/locations'
    const response = await fetch(url, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'X-API-Key': apiKey,
            'Content-Type': 'application/json'
        }
    })
    // essentailly we are just turning the `Response` object HTTP structured response and transforming it into JSON
    return await response.json()
}


// Don't touch below this line


const apiKey = generateKey()

const locations = await getLocations()
console.log('Got some locations from the server.')
for (const location of locations) {
    console.log(`- name: ${location.name}, recommendedLevel: ${location.recommendedLevel}`)
}

function generateKey() {
    const characters = 'ABCDEF0123456789'
    let result = ''
    for (let i = 0; i < 16; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length))
    }
    return result
}

