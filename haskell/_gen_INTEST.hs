import System.Environment
import System.Random
import System.IO

minK = 1 :: Int
maxK = 10^7 :: Int 
minX = 0 :: Int
maxX = 10^9 :: Int

main = do
    args <- getArgs
    gen <- getStdGen
    let n = if args == [] then 1000 else read (head args)
        (k, gen') = randomR (minK, maxK) gen
    putStrLn (show n ++ " " ++ show k)
    printRandomRs (minX, maxX) gen' n

printRandomRs :: RandomGen g => (Int, Int) -> g -> Int -> IO ()
printRandomRs _ _ 0 = return ()
printRandomRs r gen n = do
    let (x, gen') = randomR r gen
    print x
    printRandomRs r gen' (n-1)
