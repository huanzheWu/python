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


def addressBook(name , phone ,Class="计算机科学与技术3班 "):
    print('name:',name)
    print('phone:',phone)
    print('Class:',Class)

def func(a,L=[]):
    L.append(a)
    return L

def func1(a=0):
    a += 1
    return a

if  __name__ == '__main__':
    # error call
    #fib(1,2)

    #print(fib(10))
    
    #arr = getfib(10)
    
    #a =  returnMore()
    #print(a)
    
   # print(arr)

  #  addressBook('小明',785496)
  #  addressBook('小红',121545)
  #  addressBook('小黑',548796,"网络工程1班")

    for i in range(10):
       print( func1(i) )


