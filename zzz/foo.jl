#!/usr/bin/julia
using UnicodePlots
f="a"
while f != "q" && f != "Q"
    x = randn(1000000)
    display(histogram(x))
    println("q or Q to quit: ")
    global f
    f = readline()
end
