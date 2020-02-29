def sumof2 (x,y):
    return lambda z:z+x+y

ref1=sumof2(12,30)
# Different arguments of print function 
print("Result from Lambda ", ref1(8))
 # concatation of strings

string1= "Result from Lambda " + str(ref1)
print(string1)
