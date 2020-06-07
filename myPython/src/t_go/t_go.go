package main

import (
	"fmt"
	//"math/rand"
	//"time"
	"runtime"
)

func hello(n int) {
	//fmt.Println("Hello World !")
	//r := rand.Intn(100)              //랜덤 수 발생
	//time.Sleep(time.Duration(r))     // 정지
	//fmt.Println(n)
}

func sum(a int, b int, c chan int) {
	c <- a + b
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	c := make(chan int)

	for i := 0; i < 100; i++ {
		go hello(i)
	}
	go sum(1, 2, c)
	go func() {
		n := <-c
		fmt.Println(n)
	}()

	fmt.Println(runtime.GOMAXPROCS(1))

	fmt.Scanln()

}
