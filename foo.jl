println("hello, julia")
function fibo(n)
	a, b = 0, 1
	f = []
	while b <= n
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

