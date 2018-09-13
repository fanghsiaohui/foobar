using Plots
unicodeplots()
x = 1:100
y1 = cos.(x)
y2 = log.(x)
println(x)
p1 = plot(x,y1)
p2 = plot!(x, y2)
display(p2)
println(y2)

#=
# pi
function p(n)
	m = 0
	for i in 1:n
		x, y = rand(), rand()
		if (2x-1)^2 + (2y-1)^2 <= 1
			m += 1
		end
	end
	return 4m/n
end
=#

#=
function Babylonian(x; N = 10) 
    t = (1+x)/2
    for i = 2:N; t=(t + x/t)/2  end    
    t
end
x=2; Babylonian(x),√x
using Plots
pyplot()
i = 0:.01:49
p=plot([x->Babylonian(x,N=i) for i=1:5],i,label=["Iteration $j" for i=1:1,j=1:5])
display(p)
=#
#plot!(sqrt,i,c="black",label="sqrt",
#      title = "Those Babylonians really knew how to √")

#= a simple test function
println("hello, julia")
function fibo(n)
	a, b = 0, 1
	f = []
	while b <= n
        	print(b, ' ')
		push!(f, b)
		a, b = b, a+b
	end
	println()
	return f
end

y1 = fibo(60)
println("add a number")
push!(y1, 100)
println(y1)
=#

#= C++ code
C_code = """
#include <stddef.h>
double c_sum(size_t n, double *X) {
	double s = 0.0;
	for (size_t i = 0; i < n; ++i) {
		 s += X[i];
	}
	return s;
}
"""

const Clib = tempname()	# make a temporary file
# compile to a shared library by piping C_code to gcc
# (vorks only if you have gcc installed):
open(`gcc -fPIC -03 -msse3 -xc -shared -o $(Clib * "." * Libdl.dlext) -`, "w") do f
	print(f, C_code)
end

# define a Julia function that calls the C function
c_sum(X::Array{Float64}) = ccall(("c_sum", Clib), Float64, (Csize_t, Ptr{Float64}), length(X), X)

c_sum(a)
=#
