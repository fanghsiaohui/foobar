# #/usr/bin/env julia
# function prime(n)
#     #=
#     if n in [2,3,5,7]
#         return true
#     end
#     middle = ceil(sqrt(n))
#     if n % 2 == 0
#         return false
#     end
#     =#
#     #for i in range(3,stop=middle,step=2)
#     for i in 2:n-1
#         if n % i ==0
#             return false
#         end
#     end
#     return true
# end

# # print("enter a number: ")
# # n = readline(stdin)
# # n = parse(Int, n)
# max = 100000
# maxprime = 2
# @time begin
#     for i in 2:max
#         if prime(i)
#             global maxprime = i
#         end
#     end
# end
# println("$max , $maxprime")

# # function f()
# #     print("enter a number: ")
# #     n = parse(Int128, readline(stdin))
# #     if n < 2
# #         println("invalid number")
# #     else
# #         for i in 2:n
# #             if prime(i)
# #                 println(i)
# #             else
# #                 continue
# #             end
# #         end
# #     end
# # end

#julia
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
    end
    maxPrime = 2
    @time begin
        for i in 2:maxNumber
            if prime(i)
                global maxPrime = i
            end
        end
    end
    println("$maxNumber , $maxPrime")
end

#=
================================================
=#

# python
py"""
def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True

def pymain(m):
    maxNumber = m
    maxPrime = 2
    import datetime
    begin = datetime.datetime.now()
    for i in range(2,(maxNumber+1)):
        if prime(i):
            maxPrime = i
    end = datetime.datetime.now()
    time = end - begin
    print(maxNumber, maxPrime, time)
"""

pymain = py"pymain"

for i in 1:10
    maxNumber = 10000
    pymain(maxNumber)
end
