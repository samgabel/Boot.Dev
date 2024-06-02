// Showcase that different protocols function within the URL and that not all of them use the "authority component" `//`



function getMailtoLinkForEmail(email) {
    // mailto does NOT use the authority component
    return `mailto:${email}`
}


// don't touch below this line


let email = 'slayer@fquest.app'
console.log(`The mailto link for ${email} is: ${getMailtoLinkForEmail(email)}`)
email = 'killer@fquest.app'
console.log(`The mailto link for ${email} is: ${getMailtoLinkForEmail(email)}`)
