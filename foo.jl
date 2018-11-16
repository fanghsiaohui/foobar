#!/usr/bin/julia
function sayhi(name)
    println("hi $name, it's great to see you!")
end

function f(x)
    x^2
end

sayhi2(name)=println("hi $name, it's great to see you")
f2(x)=x^2

println("enter name: ")
name=readline()
sayhi(name)
println(f(42))
sayhi2(name)
println(f2(42))
