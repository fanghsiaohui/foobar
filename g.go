package main

import "fmt"

func main(){
    var x, s int
    for ;x<=10;x++ {
        s += x
        fmt.Printf("x=%d\ts=%d\n", x, s)
    }
}
