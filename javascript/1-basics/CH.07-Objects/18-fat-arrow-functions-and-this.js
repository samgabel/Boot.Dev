// Fat arrow functions use `this` to refer to the object that their parent scope refers to.

// In this case we should just use a regular function because we want to refer to properties within the same object



const server = {
    port: 8080,
    name: 'MovieStarz',
    // getLogs: () => {
        // return `Starting ${this.name} server on ${this.port}`
    getLogs: function() {
        return `Starting ${this.name} server on ${this.port}`
    }
}


// don't touch below this line


const logs = server.getLogs()
console.log(logs)
