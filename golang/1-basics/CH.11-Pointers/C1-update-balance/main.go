package main

import (
	"errors"
)

type customer struct {
	id      int
	balance float64
}

type transactionType string

const (
	transactionDeposit    transactionType = "deposit"
	transactionWithdrawal transactionType = "withdrawal"
)

type transaction struct {
	customerID      int
	amount          float64
	transactionType transactionType
}

// Don't touch above this line

func updateBalance(c *customer, t transaction) error {
	switch t.transactionType {
	// Deposits
	case transactionDeposit:
		c.balance += t.amount
		return nil
	// Withdrawals
	case transactionWithdrawal:
		if c.balance < t.amount {
			return errors.New("insufficient funds")
		}
		c.balance -= t.amount
		return nil
	// If no case matches either deposit or withdrawal
	default:
		return errors.New("unknown transaction type")
	}
}

