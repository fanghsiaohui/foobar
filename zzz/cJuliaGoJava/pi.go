package main
import (
    "fmt"
    "math/rand"
    "time"
)

func pi(n int) float64{
    m := 0
    for i := 0; i < n; i++ {
        x := rand.Float64()
        y := rand.Float64()
        if x * x + y * y < 1 {
            m++
        }
    }
    return float64(m)/float64(n)*4
}
func main(){
    n := 100
    for i:=0;i<5;i++ {
        n *= 10
        start := time.Now()
        p := pi(n)
        t := time.Since(start).Seconds()
        fmt.Println(n, p, t)
    }
}
