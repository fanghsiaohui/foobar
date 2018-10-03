#/usr/bin/env julia
# julia test file
function move(n,a,b,c)
    if n == 1
        println("move from $a to $c")
    elseif n < 1
        println("no, bye")
    else
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
    end
end

function hannuo(n)
    move(n, 'A', 'B', 'C')
end

hannuo(parse(Int, ARGS[1]))
