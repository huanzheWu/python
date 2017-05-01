#! /usr/bin/python
def fib(n):
    """ 打印斐波那契数列的前N项"""
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a ,b = b,a+b

    print()

if  __name__ == '__main__':
    # error call
    fib(1,2)
    #fib(10)
