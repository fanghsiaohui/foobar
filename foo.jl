#/usr/bin/env julia
function fWhile()
    i = 1
    while i < 10
        println(i)
        i += 1
    end
end

function fFor()
    m = 0
    for i in 1:10
        println(i)
        m += i
    end
    println(m)
end

