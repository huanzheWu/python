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






 

