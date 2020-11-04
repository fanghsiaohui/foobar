package main
import (
    "fmt"
    "math"
)

func main(){
    fmt.Println("hello, world")
    fmt.Println(math.Pi)
    a, b := 0, 1
    for i:=1;i<=10;i++ {
        a, b= b, a+b
        fmt.Println(a)
    }
}
