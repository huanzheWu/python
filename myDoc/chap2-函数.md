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


# 可变的参数列表
在Python很容易让函数拥有可变的参数列表。可变参数指的是传递给函数的参数个数是可变的，可以是0个或任意多个。例如现在需要一个函数，来录入一个班级所有同学的名字，一般的做法是我们可以先把这些名字都存储在list或者tuple之后传递给参数：
```
def registerName(Class ,names):
    print("class {0} has students:".format(Class))
    for name in names:
        print(name)

if  __name__ == '__main__':
	names = ["barry","larry","nancy","maple"]
	registerName(3,names)

# output:
class 3 has students:
barry
larry
nancy
maple
```

而如果使用了可变参数之后，就不需要我们自己封装一个list或tuple来存储学生的名字了，可以这样来调用函数：
```
def registerName1(Class,*names):
    print("class {0} has students:".format(Class))
    for name in names:
        print(name)

if  __name__ == '__main__':
  registerName1(3,"barry","larry","nancy","maple")

#output：
class 3 has students:
barry
larry
nancy
maple
	
```

可变参数是把调用函数的参数都封装成一个tuple后传递给函数，因此在函数内部接受到的是一个tuple数据结构。为了使得一个参数成为可变参数，只需要在该参数前面加上`*`即可。

# 关键字参数
在函数参数前面加上一个`*`便可以成为可变参数，那么加上`**`呢？这就引出了本节的知识点——关键字参数。我们可以对关键字参数赋予0或任意多个`keyword=value`形式的值。考虑现在需要一个函数来录入班级同学的学号，我们需要存储姓名与学号的对应关系：
```

def registerNumber(Class  , ** stuNum):
    print("class {0} 's student number:".format(Class))
    print(stuNum)

if  __name__ == '__main__':

   registerNumber(3,barry=11234,larry=22341,nancy=22351,maple=99810)

#output:
class 3 's student number:
{'barry': 11234, 'maple': 99810, 'larry': 22341, 'nancy': 22351}
```

可以看到，在`registerNumber`函数的内部，实际上接收到是是一个字典数据结构，与可变参数类似，我们也可以自己把数据放在一个字典中，然后来调用函数，调用函数的时候在字典变量前加上`**`便可将它传递给关键字参数：

```
if  __name__ == '__main__':
    stuNum = {'barry':11234,'larry':22341,'nancy':22351,'maple':99810}
    registerNumber(3,**stuNum)

#output:
class 3 's student number:
{'maple': 99810, 'barry': 11234, 'larry': 22341, 'nancy': 22351}

```
同样的道理，如果你这时拥有一个list或者tuple变量，想把它传递给可变参数，只需要在变量前加上`*`即可。

无论是可变参数还是关键字参数，都为函数提供了一种可拓展的能力，有时候我们无法确定参数的个数，例如班级同学的个数是不确定的，这时候它们就派上用场了。如果你使用过C语言的话，我们传递给main函数的参数，都会保存在main函数的argv[]参数里面，这类似于python中的可变参数。



# Lambda表达式
Lambda表达式提供了一种创建匿名函数的方法。这种功能在函数式编程语言中出现，可以用于创建匿名函数。在python中，由于语法的限制，Lambda只能写成一行，例如：
```
def returnFunc():
    return lambda n:n*n


if  __name__ == '__main__':
    f = returnFunc()
    print(f(2))
    print(f(4))
# output：
4
16
```
函数`returnFunc()`返回了一个匿名函数，这个函数赋值给f后就可以调用了，该匿名函数的功能是计算一个数的平方。而Lambda的另一个用途是将一个小函数作为参数来进行传递。关于函数式编程，可以看看
[阮一峰-函数式编程入门教程](http://www.ruanyifeng.com/blog/2017/02/fp-tutorial.html)


(完)

















 

