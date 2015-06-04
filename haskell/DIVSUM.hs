{-
SPOJ Problem Set (tutorial)

74. Divisor Summation

Problem code: DIVSUM
 
Given a natural number n (1 <= n <= 500000), please output the summation of all its proper divisors.

Definition: A proper divisor of a natural number is the divisor that is strictly less than the number.

e.g. number 20 has 5 proper divisors: 1, 2, 4, 5, 10, and the divisor summation is: 1 + 2 + 4 + 5 + 10 = 22.

Input

An integer stating the number of test cases (equal to about 200000), and that many lines follow, each containing one integer between 1 and 500000 inclusive.

Output

One integer each line: the divisor summation of the integer given respectively.

Example

Sample Input:
3
2
10
20

Sample Output:
1
8
22
-}

import qualified Data.ByteString.Lazy.Char8 as BS
import Data.List

sumDivisors :: Int -> Int
sumDivisors n = 1 + (sum $ nub $ concat [ [d, n `div` d] | d <- [2..limit], n `mod` d == 0 ])
    where limit = (floor . sqrt . fromIntegral) n

readInt :: BS.ByteString -> Int
readInt x =
    case BS.readInt x of
        Just (i,_) -> i
        Nothing    -> error "Unparsable Int"

main = do
    (w:ws) <- fmap BS.words BS.getContents
    let n = readInt w
        nums = map (sumDivisors . readInt) $ take n ws
    mapM_ print nums


{-
import System.IO
import Control.Monad
import Data.List

Original: Too slow for SPOJ

sumDivisors :: Integer -> Integer
sumDivisors n = 1 + (sum $ nub $ concat [ [d, n `div` d] | d <- [2..limit], n `mod` d == 0 ])
    where limit = (floor . sqrt . fromIntegral) n

main = do
    casesStr <- getLine
    let cases = read casesStr
    forM [1..cases] (\_ -> do
        numberStr <- getLine
        let number = read numberStr
        print $ sumDivisors number)

-}
