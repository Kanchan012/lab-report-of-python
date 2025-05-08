a=5
b=5
c=10
result=(a==b) and (c>b)
print("a==b and c>b is:",result)

result=(a==b) and (c<b)
print("a==b and c<b is:",result)

result=(a==b) or (c>b)
print("a==b or c>b is:",result)

result=(a==b) or (c<b)
print("a==b or c<b is:",result)

print("not a>b:",not(a>b))
print("not c>a:",not(c>a))

