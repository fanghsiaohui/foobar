#!/usr/bin/julia
using Dates
startTime=Dates.now()
x=rand(100,100)
y=rand(100,100)
xy=x*y
println(length(xy))
endTime=Dates.now()
println(endTime-startTime)
