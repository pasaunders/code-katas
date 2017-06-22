module Fusc where

fusc :: Int -> Int
fusc 0 = 0
fusc 1 = 1
fusc n
  | even n = fusc (n `div` 2)
  | odd n = fusc ((n-1) `div` 2) + fusc (((n-1) `div` 2) + 1)