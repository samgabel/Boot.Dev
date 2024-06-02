// We want to test out Cloudflare's DNS lookup API



async function fetchIPAddress(domain) {
    const resp = await fetch(`https://cloudflare-dns.com/dns-query?name=${domain}&type=A`, {
        headers: {
            'accept': 'application/dns-json'
        }
    })
    const respObject = await resp.json()

    // Get "Answer" property
    if (!respObject.Answer) {
        throw new Error('Invalid domain or publicly inaccessible domain')
    }

    // Get "data" property from Answer object
    for (const record of respObject.Answer) {
        if (record.data) {
            return record.data
        }
    }
    throw new Error('No valid "data" property found within "Answer" property')
}


// don't touch below this line


const domain = 'api.boot.dev'

try {
    const ipAddress = await fetchIPAddress(domain)
    console.log(`found IP address for domain ${domain}: ${ipAddress}`)
} catch (err) {
    console.log(err.message)
}
