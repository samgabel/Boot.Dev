// Declaring a variable with `const` leads to an immutable variable
// `let` allows for the variable contents to be changed



const email = 'johndoe'

email += '@gmail.com'

// don't touch below this line

console.log(email)
// this will give us a TypeError: Assignment to constant variable
