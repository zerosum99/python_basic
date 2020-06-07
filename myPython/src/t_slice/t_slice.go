package main

import "fmt"

func main() {

	var s_x []int

	fmt.Println(" empty slice ", s_x, len(s_x), cap(s_x))
	s_a := make([]int, 5, 5)
	s_b := s_a[2:4]
	s_c := make([]int, len(s_b), len(s_b))

	fmt.Println(len(s_c), cap(s_c))

	var x interface{}
	var s SInter

	var y MyInt = 1
	x = y

	s = y

	s.add(y)

	fmt.Println("yyyyy", x)
	x.(MyInt).add(y)
	y.add(y)
}

type SInter interface {
	add(MyInt)
}

type MyInt int

func (this MyInt) add(j MyInt) {

	fmt.Println("add func ", this+j)
}
