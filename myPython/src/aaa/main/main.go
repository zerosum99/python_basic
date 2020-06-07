package main

import (
	"aaa/add"
	"aaa/add/sub"
	"aaa/multi"
	"aaa/multi/div"
	"fmt"
	"reflect"
)

type data struct {
	id   [13]byte
	name [20]byte
}

func (this *data) Set(any []byte) {
	copy(this.id[:], any[0:13])
	copy(this.name[:], any[13:33])
}

type List []interface{}

func add11(x, y int) int {
	return x + y
}

func (l List) Accumulate(f Operation) interface{} {
	res := 0
	for _, v := range l {
		if i, ok := v.(int); ok {
			res = f(res, i)
			continue
		}
		if lst, ok := v.(List); ok {
			res = f(res, lst.Accumulate(f).(int))
		}
	}
	return res
}

type Operation func(int, int) int

func main() {
	fmt.Println("hello world ")
	fmt.Println(" add ", add.Add(3, 3))
	fmt.Println(" subb ", add.Subb(3, 3))
	fmt.Println(" sub ", sub.Sub(6, 3))
	fmt.Println(" multi ", add.Multi(6, 3))
	fmt.Println(" mul ", multi.Mul(6, 4))
	fmt.Println(" div ", div.Div(6, 2))

	fmt.Println("")

	var mapping []byte = make([]byte, 33)
	mapping = []byte("0123456789012abcdefghijklmnopqrstuvxyz3456789")

	a := new(data)

	a.Set(mapping)
	fmt.Println(" id ", string([]byte(a.id[:])))
	fmt.Println(" name ", string([]byte(a.name[:])))
	fmt.Println(" mapping ", string(mapping))

	var abb [20]byte
	copy(abb[:], []byte("hello world"))
	fmt.Println(string(abb[:]))

	var xxx int
	fmt.Println(" xxx address ", &xxx)
	fmt.Println(" xxx value ", reflect.ValueOf(xxx))
	fmt.Println(" xxx value ", reflect.ValueOf(xxx).Int())
	fmt.Println(" xxx value ", reflect.TypeOf(xxx).Name())

	fmt.Println(" literal type ", reflect.TypeOf("Hello world").Name())
	fmt.Println(" literal Value ", reflect.ValueOf("Hello world"))

	fmt.Println(" literal Value ", reflect.ValueOf("Hello world").String())

	var inf interface{}
	inf = 1
	fmt.Println("interface type ", reflect.TypeOf(inf).Name())
	fmt.Println(" interface Value ", reflect.ValueOf(inf))
	fmt.Println(" literal Value ", reflect.ValueOf(inf).Int())
	fmt.Println(" interface Value ", reflect.ValueOf(1))
	fmt.Println(" literal address ", &inf)

	var x_int int
	fmt.Println(" variable declaration address", &x_int)
	fmt.Println(" variable declaration value", x_int)

	y_int := 0
	fmt.Println(" variable declaration address", &y_int)
	fmt.Println(" variable declaration value", y_int)

	type x_st struct {
		a int
		b int
	}

	var s_st x_st = x_st{10, 10}
	fmt.Println(" structure address ", &s_st)
	fmt.Println(" structure type ", reflect.TypeOf(s_st).Name())
	fmt.Println(" structure value ", reflect.ValueOf(s_st))
	fmt.Println(" structure value ", reflect.ValueOf(s_st).FieldByName("a").Int())

	x_slice := []int{1, 2, 3, 4, 5}
	var x_inf interface{}
	x_inf = &x_slice

	fmt.Println(" Elem ", reflect.ValueOf(x_inf).Elem().Index(0).Int())

	fmt.Println(" arrat Elem ", reflect.ValueOf(&[5]int{1, 2, 3}).Elem().Index(0).Int())
	fmt.Println(" arrat  ", reflect.ValueOf([5]int{1, 2, 3}).Index(0).Int())

	var x int = 1
	var y int = 2

	var in interface{}
	//var out interface{}

	in = x

	y = in.(int)

	fmt.Println(" interface type assertion ", y)

	l := List{1, 2, 3, 4}
	fmt.Println(" interface type assertion type list ", l)
	fmt.Println(" list sum ", l.Accumulate(add11).(int))

	var ar1 [5]int = [5]int{1, 2, 3, 4, 5}
	var ar2 [5]int = ar1

	fmt.Println(" original array ", &ar1)
	ar2[2] = 9
	varar2 := &ar2
	fmt.Println(" copy array   ", varar2)

	var ptr *int
	var it int = 1
	fmt.Println(" Pointer ", ptr)
	ptr = &it
	fmt.Println(" copy array   ", ptr)
}
