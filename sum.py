def seriesSum (terms):
    sum=0
    for x in range(1,terms):
            sum= sum+ (x/2**x)
    print(sum)

seriesSum (10)
