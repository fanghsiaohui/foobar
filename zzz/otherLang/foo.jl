#!/usr/bin/env julia
using UnicodePlots

function f1(m=3, n=1000000,b=45)
    a = randn(m, n)
    for i in 1:m
        p = histogram(a[i,:], nbins=b)
        display(p)
        #sleep(2)
    end
    println()
    println("the end")
end

f1()
println("press Enter to exit")
readline()
