package main

import (
	"fmt"
	"runtime"
	"sort"
	_ "time"
)

type Sequence []int

// Methods required by sort.Interface.
func (s Sequence) Len() int {
	return len(s)
}
func (s Sequence) Less(i, j int) bool {
	return s[i] < s[j]
}
func (s Sequence) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

// Method for printing - sorts the elements before printing.
func (s Sequence) String() string {
	sort.Sort(s)
	str := "["
	for i, elem := range s {
		if i > 0 {
			str += " "
		}
		str += fmt.Sprint(elem)
	}
	return str + "]"
}

func hello() {
	fmt.Println(" Hello, World goroutine ")
}

func sum(a int, b int, c chan int) {
	c <- a + b
}

func main() {
	fmt.Println(" test aaa !11")

	var sqa Sequence = []int{1, 2, 3, 4, 5}

	fmt.Println(" Len ", sqa.Len())
	fmt.Println(" Squence String ", sqa.String())

	fmt.Println(" runtime GOMAXPROC ", runtime.GOMAXPROCS(runtime.NumCPU()))
	fmt.Println(" runtime GOMAXPROC ", runtime.GOMAXPROCS(0))
	fmt.Println(" runtime NumCPU ", runtime.NumCPU())

	go hello()

	c := make(chan int)
	go sum(1, 2, c)

	n := <-c

	fmt.Println(" channel recieve ", n)

	done := make(chan bool)
	count := 3

	go func() {
		for i := 0; i < count; i++ {
			done <- true
			fmt.Println(" go routine ", i)
			//time.Sleep(1 * time.Second)
		}
	}()

	for i := 0; i < count; i++ {
		<-done
		fmt.Println(" main go ", i)
	}

	fmt.Scanln()

}
