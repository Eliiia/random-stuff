-- a function that converts a roman number to integers.
-- leetcode.com/problems/roman-to-integer/

-- the main function:
-- takes a series of characters (a string), and returns an int
-- the function will assume it is a valid roman number; invalid numbers will cause weird behaviour
romanToInt :: String -> Int
romanToInt s = sum sylValues
    where sylValues = map syllableValue (syllableSplitter s)

-- split into "syllables"
syllableSplitter :: String -> [String]
syllableSplitter "" = []
syllableSplitter s = syllableFirstSplit s : syllableSplitter (drop (length (syllableFirstSplit s)) s)

-- get the first syllable 
syllableFirstSplit :: String -> String -- allows stuff like IVX; this is fine, assuming the input is a valid number
syllableFirstSplit [c]   = [c]
syllableFirstSplit (c:s) = if value c <= value (head s)
                            then c : syllableFirstSplit s
                            else [c]

-- get the value of an individual "syllable"
syllableValue :: String -> Int
syllableValue (c:n:s) = if c /= n -- if it is not just one repeating letter, then it is subtraction 
                        then
                            syllableValue (n:s) - value c
                        else
                            value c + syllableValue (n:s) -- recursive call! definitely not the best solution!
syllableValue [c] = value c -- if only one item

-- get the value of different individual characters
value :: Char -> Int
value 'I' = 1
value 'V' = 5
value 'X' = 10
value 'L' = 50
value 'C' = 100
value 'D' = 500
value 'M' = 1000