#/usr/bin/env julia
input = readline(stdin)
n = parse(Int, input)
r = 0
while n != 0
    global r = r * 10 + n % 10
    global n = div(n, 10)
end
println(r)

