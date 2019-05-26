package main
import (
    "fmt"
)

func main(){
    a, b := 0, 1
    for i := 0; i < 10; i++ {
        a, b = b, a + b
        fmt.Println(i + 1, a)
    }
}
