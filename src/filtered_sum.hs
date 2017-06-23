module Kata where

import Data.List

sumArray :: Maybe [Int] -> Int
sumArray Nothing = 0
sumArray (Just xs) = sum (drop 1 (take (length xs - 1) (sort xs)))