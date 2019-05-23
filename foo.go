package main
/*
import (
    "fmt"
    //"math"
)
*/

func main(){
    _, _, a, b := f()
    println(a, b)
    println(&a, &b)
}

func f() (int, int, string, string){
    a, b := 0, 1
    c, d := "hello", "world"
    return a, b, c, d
}
