#!/usr/bin/julia
using UnicodePlots
x = rand(10)
println(x)
println("line")
p1 = lineplot(x)
display(p1)
println("scatter")
p2 = scatterplot(x)
display(p2)
println("histogram")
p3 = histogram(x)
display(p3)
