module DescendingOrder where

import Data.Char
import Data.List

descendingOrder :: Integer -> Integer
descendingOrder x = read (map intToDigit (sortBy (flip compare) (makeDigits x)))

makeDigits :: Integer -> [Int]
makeDigits = map digitToInt . show


descendingOrder2 :: Integer -> Integer
descendingOrder2 = read . reverse . sort . show