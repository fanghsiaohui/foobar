using Dates
function f(m)
    for i in 1:20
        b = Dates.now()
        n = 1
        while n <= m
            n += 1
        end
        e = Dates.now()
        t = e - b
        println("i = $i, n = $n")
        println(t)
    end
end
