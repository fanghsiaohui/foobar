#!/usr/bin/env julia
using UnicodePlots
for i in 1:5
    a = randn(100000)
    plot = histogram(a)
    display(plot)
end
