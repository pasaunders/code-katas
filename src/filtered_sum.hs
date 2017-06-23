module Kata where

import Data.List

sumArray :: Maybe [Int] -> Int
sumArray Nothing = 0
sumArray (Just xs) = sum (drop 1 (take (length xs - 1) (sort xs)))

sumArray2 :: Maybe [Int] -> Int
sumArray2 (Just xs@(_:_:_)) = sum xs - maximum xs - minimum xs
sumArray2 _ = 0