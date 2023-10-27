-- problem 97


-- ((a * b) `mod` c) == (((a `mod` c) * (b `mod` c)) `mod` c)


--most naive solution -- it works instantly
--answer = (28433*2^7830457+1) `mod` 10^10


-- turn integer (base 10) into binary
toBin :: Int -> [Int]
toBin 0 = [0]
toBin n = reverse (helper n)
    where 
        helper :: Int -> [Int]
        helper 0 = []
        helper n = let (q,r) = n `divMod` 2 in r : helper q


-- b^p mod m = ( (b^(p-1) mod m) * (b mod m) ) mod m
bPM :: Int -> Int -> Int -> Int
bPM base power modulus = helper power
    where
        m = modulus
        b = base
        helper :: Int -> Int
        helper 0 = 1
        helper p =  (((helper (p - 1)) `mod` m) * (b `mod` m)) `mod` m


answer = ((28433 * bPM 2 7830457 (10^10)) `mod` 10^10) + 1


----
main = do

    putStrLn ""
    putStrLn "starting..."

    putStrLn ("answer: " ++ show answer)

    putStrLn "done!"

