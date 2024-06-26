# Process




## `hellogo` Module

1. Make new directory `hellogo` inside this directory `CH.12-Local-Development` and `cd` into it
2. Initialize a new module: `go mod init {REMOTE}/{USERNAME}/hellogo` -> `go mod init github.com/samgabel/hellogo`
3. Create `main.go` file and write basic "Hello world" program
4. `go run main.go` from the `hellogo` directory (this will quickly compile and execute the program, does NOT build executable)
5. `go build` (builds executable called `hellogo`)
6. Execute the binary `./hellogo`
7. `go install` to install the `hellogo` binary to the `$GOBIN`




## `mystrings` Module

1. Make a new sibling directory inside the `CH.12-Local-Development` root directory called `mystrings` and `cd` into it
2. Initialize a new module: `go mod init github.com/samgabel/mystrings`
3. Create `mystrings.go` and write a `package mystrings`
4. `go build` in the `mystrings` directory should output nothing
> Note that there was no output because without a `main.go` or `func main()`, `go build` won't build an executable from a library package.




## Update `hellogo` Module to Include `mystrings`

1. Modify the `hellogo/main.go` to `import` the `github.com/samgabel/mystrings` module and use the `Reverse()` function
2. Modify the `hellogo/go.mod` to `require` the `mystrings` module and internally reference the `mystrings` module using the `replace` keyword
3. `cd` into the `hellogo` directory and run `go build` to recompile the binary, we can now run `./hellogo` to run the updated version
> Additionally we can run the command `go mod tidy` in order to verify our `go.mod` imports




## `datetest` Module

1. Make yet another sibling directory inside the `CH.12-Local-Development` root directory called `datetest` and `cd` into it
2. Create a `main.go` and import a remote package `tinytime "github.com/wagslane/go-tinytime"`, then paste in example code
3. Initialize a new module: `go mod init github.com/samgabel/datetest`
4. Run `go get github.com/wagslane/go-tinytime` in order to install the remote dependency package to the `$GOPATH`
> Instead of using `go get ...` we can opt for `go mod tidy` command which will search for and install all missing dependencies
5. Now compile `go build` and run `./datetest`
