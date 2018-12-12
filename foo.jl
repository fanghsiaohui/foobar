#!/usr/bin/env julia
#
# fn(x) = 1/(√(2*pi)*δ)*ℯ^(((x-μ)^2)/(-2*δ^2))
function fn(x, μ, δ)
    y = 1 / (√(2*pi) * δ) * ℯ^(-(x - μ)^2 / (2 * δ^2))
    return y
end
function f(m)
    m = m
    function g(n)
        return m*n
    end
    return g
end
