#!/usr/bin/env julia
#
# f(x) = 1/(√(2*pi)*δ)*ℯ^(((x-μ)^2)/(-2*δ^2))
function f(x, μ, δ)
    y = 1 / (√(2*pi) * δ) * ℯ^(-(x - μ)^2 / (2 * δ^2))
    return y
end

