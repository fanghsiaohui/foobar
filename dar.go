package main
import (
    "fmt"
    "os"
    //"net/http"
)
func main(){
    fmt.Println(len(os.Args), os.Args)
    a, b := 0, 1
    var p *int
    for i := 0; i < 10; i++ {
        a, b = b, a + b
        p = &i
        fmt.Println(i, a)
        fmt.Println(*p)
    }
    fmt.Println(*p, a)
}
