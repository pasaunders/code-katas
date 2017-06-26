module DescendingOrder where

import Data.Char
import Data.List

descendingOrder :: Integer -> Integer
descendingOrder x = read (map intToDigit (sortBy (flip compare) (makeDigits x))) :: Integer

makeDigits :: Integer -> [Int]
makeDigits = map digitToInt . show