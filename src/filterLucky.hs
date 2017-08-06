module Haskell.Codewars.LuckyNumbers where

filterLucky :: [Int] -> [Int]
filterLucky = filter findSeven

findSeven :: Int -> Bool
findSeven x = 0 < length (filter (== '7') (show x))

filterLucky2 :: [Int] -> [Int]
filterLucky2 = filter (elem '7' . show)