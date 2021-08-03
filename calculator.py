#계산기
def add(x, y):
     return x+y

def subtract(x, y):
     return x-y

def multiply(x, y):
     return x*y

def devide_new(x, y):
    return x/y

def get_Median(x, y):
    return(x+y)/2

def get_Reminder(x, y):
    return x//b

def get_Abs(num):
    if num>=0:
        return num
    else:
        return -num

def get_percent(x, y):
    return (x/y) * 100

def get_Sum_ver1(n):
    return n(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num *n
        n = n- 1
    return num