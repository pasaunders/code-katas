module Codewars.G964.Countdig where

import Data.Char

nbDig :: Int -> Int -> Int
nbDig n d = foldr (+) 0 (map  (\a -> stringDigits (show (a^2)) d) [0..n])

stringDigits :: String -> Int -> Int
stringDigits num digit = length (filter (== intToDigit digit) num)

nbDig2 :: Int -> Int -> Int
nbDig2 n d = sum [length $ filter (==c) $ show (x*x) | x <- [0..n]]
  where c = intToDigit d