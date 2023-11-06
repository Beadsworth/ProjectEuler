-- problem 816


import Data.List


-- point generator
-- be careful about redundant calls to s!
sList :: Int -> [Int]
sList n = reverse (sL n)
    where
        sL :: Int -> [Int]
        sL 0 = 290797 : []
        sL n = (((head a)^2) `mod` 50515093) : a
            where
                a = sL (n-1)


d :: Int -> [(Int, Int)]
d k = zip sEven sOdd
    where
        n = k + 1
        s = sList (2*n)
        sEven = evens s
        sOdd = odds s


-- basic math & comp
dist2 :: (Int, Int) -> (Int, Int) -> Int
dist2 (x1, y1) (x2, y2) = (a^2 + b^2)
    where 
        a = (x2-x1)
        b = (y2-y1)


dist :: (Int, Int) -> (Int, Int) -> Double
dist (x1, y1) (x2, y2) = sqrt (fromIntegral (dist2 (x1, y1) (x2, y2)))


enumerate x = zip [0..] x
evens xs = [x | (i, x) <- enumerate xs, even i]
odds xs = [x | (i, x) <- enumerate xs, odd i]


-- sort by coords
-- usage: sortBy xCoord someList
xCoord (x1, y1) (x2, y2) = compare x1 x2
yCoord (x1, y1) (x2, y2) = compare y1 y2


-- find index of first occurance greater than value
binSearchGtIndex :: Int -> [Int] -> Int
binSearchGtIndex value [] = error "list is empty"
binSearchGtIndex value list
    | value > (last list) = length list
    | otherwise  = binSearchGtIndexHelper value enumeratedList
        where
            enumeratedList = enumerate list


binSearchGtIndexHelper :: Int -> [(Int, Int)] -> Int
binSearchGtIndexHelper value enumeratedList
    | n == 1 = i
    | last_l < value = binSearchGtIndexHelper value r
    | otherwise = binSearchGtIndexHelper value l
        where
            n = length enumeratedList
            half = n `div` 2
            l = take half enumeratedList
            r = drop half enumeratedList
            last_l = snd (last l)
            i = fst (head enumeratedList)


-- wrapper
closestDist :: [(Int, Int)] -> Double
closestDist list_Z = sqrt (fromIntegral answerDist2)
    where
        list_X' = sortBy xCoord list_Z
        answerDist2 = closestPair list_X'


qList :: (Int, Int) -> Int -> [(Int, Int)] -> [(Int, Int)]
qList point delta sortedPointList = q
    where
        (px, py) = point
        min_qy = py - 2 * delta
        qyList = [y | (x, y) <- sortedPointList]
        min_qy_index = binSearchGtIndex min_qy qyList
        q = take 6 (drop min_qy_index sortedPointList)


-- divide and conquer algo
closestPair :: [(Int, Int)] -> Int
closestPair list_X
    | n == 2 = (dist2 (list_X !! 0) (list_X !! 1))
    | n == 3 = minimum [(dist2 (list_X !! 0) (list_X !! 1)), (dist2 (list_X !! 1) (list_X !! 2)), (dist2 (list_X !! 2) (list_X !! 0))]
    | otherwise = minimum [d, dz] 
        where
            -- split list in half
            n = length list_X
            half = n `div` 2
            l = take half list_X
            r = drop half list_X
            
            -- find minimum of each half
            dl = closestPair l
            dr = closestPair r
            d = minimum [dl, dr]

            -- points within range d of x_mid
            (x_mid, y_mid) = head r
            xLower = (fromIntegral x_mid) - d
            xUpper = (fromIntegral x_mid) + d

            -- there's potential to speed this up, stop collecting once bounds are found
            lx = [x | (x, y) <- l]
            blIndex = binSearchGtIndex xLower lx
            bl = drop blIndex l
            br = [(x, y) | (x, y) <- r, x <= xUpper]
            brs = sortBy yCoord br

            -- check 6 remaining candidates    
            candidates = [dist2 p q | p <- bl, q <- qList p d brs]
            dz = if (length candidates) > 0 then (minimum candidates) else d

-- test_case
test_case = closestDist listZ
    where
        listZ = d 14

-- solve the problem
answer = closestDist list_Z
    where
        list_Z = d 2000000


----
main = do

    putStrLn ""
    putStrLn "thinking..."

    putStrLn ("test_case: " ++ show test_case)
    putStrLn ("answer: " ++ show answer)

    putStrLn "done!"

