-- problem 63


-- an n-digit-long number can be between (10^(n-1)) and ((10^n) - 1)
-- The upper bound for a^n must be (10^n-1)
-- (a^n) < (10^n) implies a < 10
-- a is [1..9]
max_a = 9


-- upper bound for n is set by (a^n) > 10^(n-1)
-- 1 / (1 - log10(a)) > n
-- for a = 9, n must be less than or equal to 21

-- for the form (a^n)
max_n = floor (1 / (1 - (logBase 10 max_a)))


-- don't forget to concat 1, since it also satisfies the requirements
powerful_numbers = 1:[a^n | a <- [1..9], n <-[1..max_n], (10^(n-1))< a^n, (a^n)<(10^n)]

-- length of list
answer = sum [1 | x <- powerful_numbers]


----
main = do
    putStrLn "starting problem 63..."

    putStrLn ("powerful_numbers: " ++ show (powerful_numbers))
    putStrLn ("answer: " ++ show (answer))

    putStrLn "done!"
