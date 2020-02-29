def func(arg1,arg2):
  return lambda x: x+ arg1+ arg2
ref1=func(12,23)
for x in range(1,5+1):
    print("result is", ref1(x))

