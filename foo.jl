#!/usr/bin/julia
using Dates
n = 100000
try
    global n = parse(Int, ARGS[1])
catch
    println("invalid input")
end
println("n=$n")
l = repeat(['a'], n)
startTime = Dates.now()
for i in 1:n
    l[i] += rand(0:25)
end
endTime = Dates.now()
tm = endTime - startTime
println("time = $tm")
println(l[end-9:end])
println(length(l)/10000)
