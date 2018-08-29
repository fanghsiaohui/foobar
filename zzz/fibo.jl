println("hello, julia")
function fibo(n)
	a, b = 0, 1
	f = []
	while b <= n
		push!(f, b)
		a, b = b, a+b
	end
	return f
end