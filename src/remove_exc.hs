module Kata where

remove :: String -> String
remove sentence
  |  head (reverse sentence) == '!' = init sentence
  | otherwise = sentence


-- Of course there's a last builtin. Using this from now on.
remove2 :: String -> String
remove2 xs
  | last xs == '!' = init xs
  | otherwise = xs