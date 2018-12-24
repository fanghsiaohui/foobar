function prime(num)
    if num <= 1
        return false
    elseif num == 2
        return true
    end
    m = sqrt(num)
    bb = true
    for i in 2:(floor(m) + 1)
        if num % i == 0
            bb = false
            break
        end
    end
    return bb
end

function monisen(no)
    i = 1
    while no > 0
        i += 1
        if prime(i) && prime(2^i - 1)
            no -= 1
        end
    end
    return (2^i -1)
end

println(monisen(parse(Int128, ARGS[1])))
