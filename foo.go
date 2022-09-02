package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	fmt.Println("hello, world")
	fmt.Print(s(os.Args[1], os.Args[2]))
}

func s(a string, b string) int {
	m, _ := strconv.Atoi(a)
	n, _ := strconv.Atoi(b)
	return m + n
}
