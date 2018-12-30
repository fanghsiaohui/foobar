#!/usr/bin/env julia
using Plots
unicodeplots()

function f(x, μ=0, δ=1)
    y = 1 / (√(2*pi) * δ) * ℯ^(-(x - μ)^2 / (2 * δ^2))
end

p = plot(f)
display(p)
