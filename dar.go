package main
import (
    "fmt"
    //"os"
    //"net/http"
)
func main(){
    a, b := 0, 1
    for i := 0; i < 30; i++ {
        a, b = b, a + b
        fmt.Printf("%3d: %12d\n", i, a)
    }
}

func f()
