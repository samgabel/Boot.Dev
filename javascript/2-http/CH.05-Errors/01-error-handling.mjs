// the "thrown" `Error` object has a property called `.message` that will print out the Error message specified when thrown



try {
    printCharacterStats(4)
    printCharacterStats('ten')
    printCharacterStats(10)
} catch (err) {
    console.log(`Message: ${err.message}`)
}


// don't touch below this line


function printCharacterStats(level) {
    if (isNaN(level)) {
        throw new Error('Parameter is not a number!')
    }
    console.log(`Your character is level ${level}!`)
}
