

###
#= fibo function
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

#=
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