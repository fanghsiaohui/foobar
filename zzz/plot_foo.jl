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

using Plots
pyplot()
x = 1:11
p1 = plot(x,y1)
y2 = rand(11)
p2 = scatter(x,y2)
display(p1)
