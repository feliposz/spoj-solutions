import qualified Data.ByteString.Lazy.Char8 as BS
 
main :: IO ()
main = do
  contents <- BS.getContents -- all IO in one go
  BS.putStr contents
