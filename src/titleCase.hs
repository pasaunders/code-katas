module TitleCase (titleCase) where

import Data.Char

titleCase :: String -> String -> String
titleCase _ "" = ""
titleCase minor sentence = unwords ((toUpper (head firstWord) : (map toLower (tail firstWord))) : map (findMinor minor) (tail wordList))
  where wordList = words sentence
        firstWord = head wordList

findMinor :: String -> String -> String
findMinor minor ys
  | ys == "" = ""
  | map toLower ys `elem`  (words (map toLower minor)) = map toLower ys
  | otherwise = toUpper (head ys) : map toLower (tail ys)


-- much more readable version from codewars answers
import Data.List (find)
import Data.Char (toUpper, toLower)

capitalize :: String -> String
capitalize (c:cs) = toUpper c : map toLower cs
capitalize     [] = []

titleCase2 :: String -> String -> String
titleCase2 minor = unwords . process . words
  where
    process :: [String] -> [String]
    process [] = []
    process (w:ws) = capitalize w : map checkNotMinor ws

    checkNotMinor :: String -> String
    checkNotMinor w = maybe (capitalize w) id $ find (== normalize w) normalizedMinors

    normalizedMinors :: [String]
    normalizedMinors = map normalize (words minor)

    normalize :: String -> String
    normalize = map toLower