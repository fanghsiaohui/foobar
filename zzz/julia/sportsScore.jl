#!/usr/bin/julia
function printInfo()
    println("play games")
    println("need ability of players")
end

function getInputs()
    println("ability of player A (0-1):")
    a = parse(Float64, readline())
    println("ability of player B (0-1):")
    b = parse(Float64, readline())
    println("number: ")
    n = parse(Int, readline())
    return a, b, n
end

function simNGames(n, probA, probB)
    winsA, winsB = 0, 0
    for i in 1:n
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB
            winsA += 1
        else
            winsB += 1
        end
    end
    return winsA, winsB
end

function simOneGame(probA, probB)
    scoreA, scoreB = 0, 0
    serving = "A"
    while ! gameOver(scoreA, scoreB)
        if serving == "A"
            if rand() < probA
                scoreA += 1
            else
                serving = "B"
            end
        else
            if rand() < probB
                scoreB += 1
            else
                serving = "A"
            end
        end
    end
    return scoreA, scoreB
end

function gameOver(a, b)
    return (a==15 || b==15)
end

function printSummary(winsA, winsB)
    n = winsA + winsB
    println("summary: $n")
    println("player A win: $winsA, $(winsA/n)")
    println("player B win: $winsB, $(winsB/n)")
end

function main()
    printInfo()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
end
main()
