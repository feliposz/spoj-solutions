{-
SPOJ Problem Set (tutorial)

450. Enormous Input Test

Problem code: INTEST
 
The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.

Input

The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.

Output

Write a single integer to output, denoting how many integers ti are divisible by k.

Example

Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
-}

-- Solution 1: slightly modified by me for clarity
import qualified Data.ByteString.Lazy.Char8 as BS

main :: IO ()
main = do
    (w1:w2:ws) <- fmap BS.words BS.getContents
    let n = readInt w1
        k = readInt w2
        xs = map readInt $ take n ws
        answer = length [ x | x <- xs, x `mod` k == 0 ]
    print answer

readInt :: BS.ByteString -> Int
readInt x =
    case BS.readInt x of
        Just (i,_) -> i
        Nothing    -> error "Unparsable Int"



{-

-- My version (time limit exceeded):

main = do
    [n,k] <- fmap words getLine 
    answer <- process (readInt n) (readInt k) 0
    print answer

process :: Int -> Int -> Int -> IO Int
process n k acc = do
    if n == 0
        then return acc
        else do 
            x <- fmap readInt getLine
            process (n-1) k (if x `mod` k == 0 then acc+1 else acc)

-- Solution 0 from http://www.haskell.org/haskellwiki/SPOJ

main :: IO ()
main = do
    (w1:w2:ws) <- fmap words getContents
    let n = readInt w1
        k = readInt w2
        xs = map readInt $ take n ws
        count = foldl' (countDivisible k) 0 xs
    print count

countDivisible :: Int -> Int -> Int -> Int
countDivisible k acc x
    | x `mod` k == 0 = acc + 1
    | otherwise      = acc

readInt :: String -> Int
readInt = read

-- Solution 1 from http://www.haskell.org/haskellwiki/SPOJ

main :: IO ()
main = do
  (l:ls) <- BS.lines `fmap` BS.getContents -- all IO in one go
  let [n,k] = map readInt (BS.split ' ' l)
  print . length . filter ((== 0) . (`mod` k) . readInt) $ take n ls
 
readInt :: BS.ByteString -> Int
readInt x =
  case BS.readInt x of Just (i,_) -> i
                       Nothing    -> error "Unparsable Int"
-- 6.29 seconds on SPOJ


-}