#julia
using BenchmarkTools, Dates, PyCall, Printf
function prime(n)
    for i in 2:n-1
        if n % i ==0
            return false
        end
    end
    return true
end

function jlmain(m)
    maxNumber = m
    global maxPrime = 2
    for i in 2:maxNumber
        if prime(i)
            maxPrime = i
        end
    end
    println("$maxNumber , $maxPrime")
end

#=
================================================
=#

#python
py"""
import datetime
def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def pymain(m):
    maxNumber = m
    maxPrime = 2
    for i in range(2,(maxNumber+1)):
        if prime(i):
            maxPrime = i
    print(maxNumber, maxPrime)
"""
pyprime = py"prime"
pymain = py"pymain"

#=
================================================
=#

for i in 1:3
    maxNumber = 5000
    println("$i, julia:")
    a = Dates.time()
    jlmain(maxNumber)
    b = Dates.time()
    println("$((b-a)*1000)ms")
    println("=====================")
    println("$i, python:")
    a = Dates.time()
    pymain(maxNumber)
    b = Dates.time()
    println("$((b-a)*1000)ms")
    println("=====================")
end