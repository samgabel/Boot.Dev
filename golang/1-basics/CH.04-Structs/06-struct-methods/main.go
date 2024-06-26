// Essentially we define struct methods as functions outside the struct body
// The method syntax is a little different: `func (parameterName structName) methodName() returnType`



package main

type authenticationInfo struct {
	username string
	password string
}

// create the method below

// (a authenticationInfo) is the `reciever` which is a special kind of function parameter
func (a authenticationInfo) getBasicAuth() string {
	return "Authorization: Basic " + a.username + ":" + a.password
}
