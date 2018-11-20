#!/usr/bin/julia
function timer(n=5)
    println("n=$n")
    while n >= 1
        println(n)
        sleep(1)
        n -= 1
    end
    println(0)
    println("n=$n")
    return n
end
timer()
