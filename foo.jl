# #/usr/bin/env julia
using Dates
function f(n)
    starttime = Dates.now()
    for i in 1:n
        m = i^2
        if m == n^2
            println("$i, $m")
        end
    end
    endtime = Dates.now()
    lasttime = endtime - starttime
    println(lasttime)
end

# n = parse(Int, ARGS[1])
for i in 1:8
    println(i)
    n = 10^i
    f(n)
    println("========")
end
