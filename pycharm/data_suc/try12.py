

a= "65536"
#a=list(map(int,b))
res = [a[i: j]
       for i in range(len(a))
       for j in range(i + 1, len(a) + 1)]

print(str(res))