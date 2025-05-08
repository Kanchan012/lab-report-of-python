a=10
b=0
try:
    c=a/b
except:
    print("Can't divide by zero")    
else:
    print("This is else part")  
finally:
    print("This is always executed")