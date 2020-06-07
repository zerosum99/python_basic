package add

import (
	"aaa/add/sub"
	"aaa/multi"
)

func Add(x, y int) int {
	return x + y
}

func Subb(x, y int) int {
	return sub.Sub(x, y)
}

func Multi(x, y int) int {
	return multi.Mul(x, y)
}
