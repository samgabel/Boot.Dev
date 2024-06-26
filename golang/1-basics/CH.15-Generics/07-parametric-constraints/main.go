// Parametric Constraints are a way to increase granularity of generics by specifying the struct method's parameter type constrainsts
// In this case, the `biller` interface only allows structs that contain `Charge(of type customer)` where `customer` is implemented by `user` and `org`

// Look through this file to sort through the implementation layers

// biller -> (userBiller, orgBiller)
// customer -> (user , org)


package main

import (
	"fmt"
)

type biller[C customer] interface {
	// We want to implement any struct with a method that has `Charge(<customer type parameter>) bill`
	Charge(C) bill
	// We want to implement any struct with a method that has `Name() string`
	Name() string
}

// don't edit below this line

type userBiller struct {
	Plan string
}

func (ub userBiller) Charge(u user) bill {
	amount := 50.0
	if ub.Plan == "pro" {
		amount = 100.0
	}
	return bill{
		Customer: u,
		Amount:   amount,
	}
}

func (sb userBiller) Name() string {
	return fmt.Sprintf("%s user biller", sb.Plan)
}

type orgBiller struct {
	Plan string
}

func (ob orgBiller) Name() string {
	return fmt.Sprintf("%s org biller", ob.Plan)
}

func (ob orgBiller) Charge(o org) bill {
	amount := 2000.0
	if ob.Plan == "pro" {
		amount = 3000.0
	}
	return bill{
		Customer: o,
		Amount:   amount,
	}
}

type customer interface {
	GetBillingEmail() string
}

type bill struct {
	Customer customer
	Amount   float64
}

type user struct {
	UserEmail string
}

func (u user) GetBillingEmail() string {
	return u.UserEmail
}

type org struct {
	Admin user
	Name  string
}

func (o org) GetBillingEmail() string {
	return o.Admin.GetBillingEmail()
}

