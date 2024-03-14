def coinPrint(coin,str):
    if(coin==0):
        print(str)
        return
    coinPrint(coin-1,str=str +"H")
    coinPrint(coin-1,str=str +"T")

coinPrint(3,"")