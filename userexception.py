class MyException(Exception):
    pass
def checkbalance():
    money=4000
    withdraw=2000
    balance=money-withdraw
    if(balance<=1000):
        raise MyException("Insufficient balance")
    print(balance)
try:
    checkbalance()
except MyException as mye:
    print(mye)    