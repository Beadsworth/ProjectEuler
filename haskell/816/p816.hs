-- problem 816
-- reduced execution from ~ 5 minutes to ~ 25 sec


import Data.List
import Data.Array


-- point generator
-- be careful about redundant calls to s!

sList :: [Int]
sList = iterate (\s -> s ^ 2 `mod` 50515093) 290797

pList :: [(Int, Int)]
pList = unfoldr (\(x:y:zs) -> Just ((x, y), zs)) sList

d :: Int -> [(Int, Int)]
d k = take k pList


-- basic math & comp
distSquared :: (Int, Int) -> (Int, Int) -> Int
distSquared (x1, y1) (x2, y2) = (a^2 + b^2)
    where 
        a = (x2-x1)
        b = (y2-y1)


-- sort by coords
-- usage: sortBy xCoord someList
xCoord (x1, y1) (x2, y2) = compare x1 x2
yCoord (x1, y1) (x2, y2) = compare y1 y2


-- find list of 6 (max) points in candidate-zone
-- where candidate-zone is within +/- 2 * delta of the given point
-- use a binary search on the list of points sorted by y-value
candidateList :: (Int, Int) -> Int -> [(Int, Int)] -> [(Int, Int)]
candidateList point delta pointList = result
    where
        -- need list sorted by y
        sortedPointList = sortBy yCoord pointList

        -- define candidate-zone
        (px, py) = point
        yMin = py - 2 * delta
        yMax = py + 2 * delta
        
        -- create array
        iMax = (length sortedPointList) - 1
        sortedArray = listArray (0, iMax) sortedPointList

        -- binary search algo
        binarySearch :: Int -> Int -> Int -> Array Int (Int, Int) -> Int
        binarySearch lo hi value sortedArray
            | lo == hi = lo
            | yMid >= value = binarySearch lo mid value sortedArray
            | otherwise = binarySearch (mid+1) hi value sortedArray
                where
                    mid = (lo + hi) `div` 2
                    (xMid, yMid) = sortedArray ! mid

        -- lowest (in y) possible candidate
        indexStart = binarySearch 0 iMax yMin sortedArray
        
        -- beware out-of-index error
        indexStop = minimum [iMax, indexStart + 5]
        
        -- grab at most 6 candidates
        r = [sortedArray!i | i <- [indexStart..indexStop]]
        
        -- filter out any bad candidates
        result = filter (\(x, y) -> y <= yMax) r


-- divide and conquer algo
-- guide: https://www.cs.ubc.ca/~liorma/cpsc320/files/closest-points.pdf
-- assumes incoming pointList is sorted by xCoord
minDist :: [(Int, Int)] -> Int
minDist pointList
    | n == 2 = (distSquared (pointList !! 0) (pointList !! 1))
    | n == 3 = minimum [(distSquared (pointList !! 0) (pointList !! 1)), (distSquared (pointList !! 1) (pointList !! 2)), (distSquared (pointList !! 2) (pointList !! 0))]
    | otherwise = recursiveResult 
        where
            -- split list in half
            n = length pointList
            half = n `div` 2
            (l, r) = splitAt half pointList
            
            -- find minimum of each half
            dl = minDist l
            dr = minDist r
            d = minimum [dl, dr]

            -- points within range d of x_mid
            ( (x_mid, y_mid) : _ ) = r
            xLower = (fromIntegral x_mid) - d
            xUpper = (fromIntegral x_mid) + d

            -- there's potential to speed this up, stop collecting once bounds are found
            bl = [(x, y) | (x, y) <- l, xLower <= x]
            br = [(x, y) | (x, y) <- r, x <= xUpper]

            -- check 6 remaining candidates    
            distSquaredCandidates = [(distSquared p q) | p <- bl, q <- (candidateList p d br)]
            
            -- compared zone candidates to d
            recursiveResult 
                | length distSquaredCandidates > 0 = minimum [d, dz]
                | otherwise = d
                    where
                        dz = minimum distSquaredCandidates


solve :: Int -> Double
solve k = result
    where
        pointList = d k
        pointListSortedByX = sortBy xCoord pointList
        minDistSquared = minDist pointListSortedByX
        result = sqrt (fromIntegral minDistSquared)


-- solutions
test_case = solve 14
answer = solve 2_000_000


----
main = do

    putStrLn ""
    putStrLn "thinking..."

    putStrLn ("test_case: " ++ show test_case)
    putStrLn ("answer: " ++ show answer)

    putStrLn "done!"

