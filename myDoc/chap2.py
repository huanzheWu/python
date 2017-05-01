#! /usr/bin/python
def fib(n):
    """ 打印斐波那契数列的前N项"""
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a ,b = b,a+b

    print()


def getfib(n):
    a ,b = 0,1
    result=[]
    for i in range(n):
        result.append(a)
        a,b = b,a+b
    return result

def returnMore():
    a =10
    b ='marry'
    return a,b


if  __name__ == '__main__':
    # error call
    #fib(1,2) 
    #print(fib(10))
    #arr = getfib(10)
    
   
    a =  returnMore()
    print(a)
    
   # print(arr)
