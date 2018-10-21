#/usr/bin/env julia
# julia test file
using Printf

cnt = 0
function hanoi(n, a = 'A', b = 'B', c = 'C')
    if n == 1
        global cnt += 1
        #println("$cnt move $n from $a to $c")
        @printf("%2d: move %2d from %c to %c\n", cnt, n, a, c)
    elseif n < 1
        println("no, bye")
    else
        hanoi(n-1, a, c, b)
        #hanoi(1, a, b, c)
        cnt += 1
        #println("$cnt move $n from $a to $c")
        @printf("%2d: move %2d from %c to %c\n", cnt, n, a, c)
        hanoi(n-1, b, a, c)
    end
end

#hanoi(parse(Int, ARGS[1]))
hanoi(4)

