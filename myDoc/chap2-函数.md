# 定义函数

关键字`def`用来定义一个函数。`def`之后跟着函数名称以及使用圆括号`()`括起来的函数参数。函数的函数体在下一行使用缩进来书写。Python的函数没有显式的返回类型声明——这对动态语言Python来说，是正常的。下面是一个函数的例子，用于打印一个斐波那契数列的前n项：
```
def fib(n):
    """ 打印斐波那契数列的前N项"""
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a ,b = b,a+b

    print()

```
函数体的第一行称为字符串文本，可以用来对函数的功能做一个说明，有一些工具可以自动提取这些字符串，形成文档，因此这个字符串文本也称为docstring。
我们定义的这个函数仅有一个参数n，n属于位置参数。关于参数我们下面会更深入讨论。函数体实现了斐波那契数列打印。所谓的斐波那契数列，是指数列的头两项是0，1，从第三项开始，a[n]=a[n-1]+a[n-2](n>=2).例如一个10项的斐波那契数列：0 1 1 2 3 5 8 13 21 34 

# 调用函数
其实我们很早就已经调用过函数了。例如打印的函数`print`。这是Python内置的函数，我们可以直接调用。Python标准库提供了许多有用的函数供我们调用，可以从Python的官方文档中查找这些函数的说明：
[python 3.5 官方 文档](https://docs.python.org/3.5/library/index.html)

调用自定义函数时也和调用内置函数一样，例如调用`fib`函数：
```
if  __name__ == '__main__':
    
    fib(10)

#output:0 1 1 2 3 5 8 13 21 34
```
这里先不用理会` __name__ == '__main__'`是什么，只需要知道在这个语句之下的语句会得到执行即可。

对函数进行正确的调用，有几点要求：

-  调用函数的时候，要求传入的参数类型与函数体中对函数参数类型的要求相匹配。例如我们在函数体中调用了内置函数`range(n)`用于产生一个范围(0,n)，这个函数期待一个interger，如果我们把字符串传给这个函数，将得到一个`TypeError`:
```
TypeError: 'str' object cannot be interpreted as an integer
```
该错误提示我们没办法把字符串解释为一个整数。

- 函数参数数量要与函数要求的数量一致。例如`fib(n)`函数期待一个函数参数，如果这样来调用它，也会抛出`TypeError`错误：

```
if  __name__ == '__main__':
    
    fib(1,2)

# output :
Traceback (most recent call last):
  File "./chap2.py", line 13, in <module>
    fib(1,2)
TypeError: fib() takes 1 positional argument but 2 were given
```

# 函数返回值
尽管函数在定义的时候没有显式地写出函数返回值，但是Python的函数与C语言一致，可以返回数据。默认情况下，函数的返回值为`None`，我们可以使用`print`来吧`fib`函数的返回值打印出来：
```
if  __name__ == '__main__': 
	print(fib(10))

# output: 0 1 1 2 3 5 8 13 21 34 
None

```
在执行完函数`fib`后，`print`打印了函数的返回值`None`。我们可以更改`fib`函数的实现，让其返回一个斐波那契数列，而不是把数列打印出来。我们将新函数命名为`getfib`:

```
def getfib(n):
    a ,b = 0,1
    result=[]
    for i in range(n):
        result.append(a)
        a,b = b,a+b
    return result

if  __name__ == '__main__':
    arr = getfib(10)
    print(arr)

# output:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

`getfib`函数将斐波那契数列的每一项存储在链表变量`result`中，然后函数返回了这个链表。

在Python中，还可以一次返回"多个"值，例如：
```
def returnMore():
    a =10
    b ='marry'
    return a,b
```
这实际上是返回了一个Tuple，关于Tuple，我们在数据类型一节中来介绍。
```
if  __name__ == '__main__':
   
    a =  returnMore()
    print(a)
    
# output: (10, 'marry')
```

# 默认参数
在Python中，定义函数的时候可以指定函数的参数默认值，这些参数称为默认参数。调用函数的时候，如果没有默认参数对应的实参，那么默认参数的值将为指定的默认值.

假设现在我要把班上同学的信息录入通讯录中，为此我需要实现一个函数。默认情况下，我这个班级上的每一个同学都属于'计科3班',但也无法避免这个函数被计科3班之外的班级所使用，所以最好的办法是把班级这个参数设置为默认参数，默认值为'计科3班'：


```

def addressBook(name , phone ,Class="Computer Science 3 "):
    print('name:',name)
    print('phone:',phone)
    print('Class:',Class)

```
然后在录入同学信息时候，就可以这样来调用：

```

if  __name__ == '__main__':

    addressBook('小明',785496)
    addressBook('小红',121545)
    addressBook('小黑',548796,"网络工程1班")

# output:
name: 小明
phone: 785496
Class: 计算机科学与技术3班 
name: 小红
phone: 121545
Class: 计算机科学与技术3班 
name: 小黑
phone: 548796
Class: 网络工程1班

```

需要注意的是，默认参数只能放在函数参数列表的尾部，如果有多个函数默认参数，它们都需要处于函数的尾部，例如：
```
def deffunc(a , b = 1, c = 2,d = 3):
	pass

```
另外一点需要注意的是，默认值只会被赋予一次。这句话有点费解，我们来看一个例子：

```
def func(a,L=[]):
    L.append(a)
    return L


if  __name__ == '__main__':	
    for i in range(10):
        print(func(i))

#output :

[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```
原因是这样的，默认参数只在函数定义的时候被赋予初值。`L`是一个变量，在函数定义时它指向了可变对象`[]`,之后的每次函数调用中，可变对象`[]`i都被添加了一个新整数。所以在使用默认参数时，切记默认参数必须指向不变的对象。

















 

