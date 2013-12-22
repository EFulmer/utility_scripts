import qualified Crypto.Hash.SHA256 as SHA256
import qualified Data.ByteString as B
import System.Environment

fileHash :: B.ByteString -> B.ByteString
fileHash bs = go SHA256.init bs
    where 
        go ctx bs 
            | bs == B.empty = SHA256.finalize ctx
            | otherwise = go (SHA256.update ctx start) rest
                    where 
                        start = B.take 8 bs
                        rest = B.drop 8 bs

main = do 
    args <- getArgs
    let fName1 = args !! 0 
        fName2 = args !! 1
    f1 <- B.readFile fName1
    f2 <- B.readFile fName2
    putStrLn $ show $ (fileHash f1) == (fileHash f2)
