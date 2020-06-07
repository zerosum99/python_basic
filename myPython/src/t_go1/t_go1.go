package main

import (
	"fmt"
	"runtime"
	//"time"
)

func main() {
	runtime.GOMAXPROCS(1)

	done := make(chan bool, 2)

	count := 4

	go func() {
		for i := 0; i < count; i++ {
			done <- true
			fmt.Println(" goroutine :", i)
			//time.Sleep(1 * time.Second) // untill one second
		}
	}()

	for i := 0; i < count; i++ {
		<-done
		fmt.Println(" main :", i)
	}

	close(done)
}
