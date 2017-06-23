module Codewars.Kata.AlternatingCase where

import Data.Char

toAlternatingCase :: String -> String
toAlternatingCase str = map switchCase str

switchCase :: Char -> Char
switchCase x
    | isLower x = toUpper x
    | isUpper x = toLower x
    | otherwise = x