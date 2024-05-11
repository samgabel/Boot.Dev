// Not all variables have a value, some don't even have a `null` value. We can declare an empty or undefined variable

// If you need a 'nonetype' value -> JUST STICK WITH `null` !!!!
// `undefined` means that the variable was never "assigned" a value


let undefinedVar

// undefined is a falsey value
console.log(undefinedVar, undefinedVar == true)

// update the value in `undefinedVar`
undefinedVar = 6

console.log(undefinedVar)
