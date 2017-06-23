module Kata where

remove :: String -> String
remove sentence
  |  head (reverse sentence) == '!' = init sentence
  | otherwise = sentencemodule Kata where


-- Of course there's a last builtin. Using this from now on.
remove :: String -> String
remove xs
  | last xs == '!' = init xs
  | otherwise = xs