// We can also use `JSON.parse()` to parse the stringified JSON back into a JavaScript Object



function parseLocation(locationString) {
    try {
        const parsedObj = JSON.parse(locationString)
        printLocationObj(parsedObj)
    } catch (err) {
        console.log(err.message)
    }
}


// don't touch below this line


function printLocationObj(parsed) {
    console.log(`id: ${parsed.id}`)
    console.log(`discovered: ${parsed.discovered}`)
    console.log(`name: ${parsed.name}`)
    console.log(`recommendedLevel: ${parsed.recommendedLevel}`)
}

parseLocation(`
{
  "discovered": false,
  "id": "0194fdc2-fa2f-4cc0-81d3-ff12045b73c8",
  "name": "Bandit Camp",
  "recommendedLevel": 14
}
`)

console.log('---')

parseLocation(`
{
  "discovered":true,
  "id":"2f8282cb-e2f9-496f-b144-c0aa4ced56db",
  "name":"Irondeep",
  "recommendedLevel":6
}
`)

console.log('---')

// we are intentionally missing a comma in this one
parseLocation(`
{
  "discovered":false,
  "id":"0f12951e-0a74-4846-a1e0-10b33b13112f"
  "name":"Tavern",
  "recommendedLevel":1
}
`)
