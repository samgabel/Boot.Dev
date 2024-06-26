module github.com/samgabel/hellogo

go 1.22.4

// we replace the remote with our local version (because we aren't deploying this to github and because the module is a sibling directory)
// NOTE that this is improper, and when/if we publish this project to github.com, we should ABSOLUTELY drop this
replace github.com/samgabel/mystrings v0.0.0 => ../mystrings

// our hellogo module relies on the mystrings module
require github.com/samgabel/mystrings v0.0.0
