-- problem 800

-- reduced from ~150 sec to ~5 sec
-- runtime is now dominated by isPrime calculations


import Data.Array (Array, (//), (!))
import qualified Data.Array as A


-- from: https://byorgey.wordpress.com/2023/01/01/competitive-programming-in-haskell-better-binary-search/
-- Discrete binary search.  Find the largest integer in [lo,hi] such
-- that monotone predicate p holds.
binarySearchD :: Int -> Int -> (Int -> Bool) -> Int
binarySearchD lo hi p
  | lo == hi        = lo
  | not (p (mid+1)) = binarySearchD lo mid p
  | otherwise       = binarySearchD (mid+1) hi p
  where
    mid = (lo + hi) `div` 2


binarySearchArray :: (Int -> Bool) -> Array Int Int -> Int
binarySearchArray p array = binarySearchD lo hi pred
    where
        (lo, hi) = A.bounds array
        pred :: Int -> Bool
        pred q = p (array ! q)


isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral


isPrime :: Int -> Bool
isPrime k
    | k < 2 = False
    | k `mod` 2 == 0 = True
    | otherwise = null [ x | x <- [3,5..isqrt k], k `mod` x == 0]


primes = 2 : [n | n <- [3,5..], isPrime n]


-- test for hybrid-integer
-- p ln q + q ln p <= expn ln base
isHI :: Int -> Int -> Int -> Int -> Bool
isHI base expn p q = (fP * (log fQ) + fQ * (log fP)) <= (fExpn * (log fBase))
    where
        fP = fromIntegral p
        fQ = fromIntegral q
        fBase = fromIntegral base
        fExpn = fromIntegral expn


-- for a given p, find the highest value of q
qUpperIndex :: Int -> Int -> Int -> Array Int Int -> Int
qUpperIndex base expn p primeArray = index
    where
        --qList = takeWhile (\q -> isHI base expn p q) primeList
        pred :: Int -> Bool
        pred q = isHI base expn p q
        index = binarySearchArray pred primeArray


-- C(n), where n = base ^ expn
c base expn = sum pCounts
    where
        -- find all possible primes used in the scenario
        primeList = takeWhile (\q -> isHI base expn 2 q) primes

        -- convert to array for binary search
        primeArray = A.listArray (0, (length primeList) - 1) primeList

        -- (p, q) pairs for which q is the next prime after p
        pQPairs = zip (take ((length primeList) - 1) primeList) (drop 1 primeList)
        pQPrimes = takeWhile (\(p, q) -> isHI base expn p q) pQPairs
        pQPrimesI = zip [0..] pQPrimes
        
        -- find upper limit of q for a given p
        qUI :: Int -> Int
        qUI p = qUpperIndex base expn p primeArray
        
        -- count primes from p (non-inclusive) to q (inclusive)
        -- at this point, you can simply take the diff between indices
        pCount :: Int -> Int -> Int
        pCount p i = (qUI p) - i

        -- iterate through all possible p values
        pCounts = [(pCount p i) | (i, (p, pNext)) <- pQPrimesI]


-- solutions
testCase0   = c 800 1
testCase1   = c 800 800
answer      = c 800800 800800


----
main = do

    putStrLn ""
    putStrLn "thinking..."

    putStrLn ("test_case: " ++ show testCase0)
    putStrLn ("test_case: " ++ show testCase1)
    putStrLn ("answer: " ++ show answer)

    putStrLn "done!"
