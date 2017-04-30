[TOC]

# if语句
条件判断语句，格式是：

```
x = input("Please enter an inter number:")
if x < 0 :
	print("x < 0 ")
elif x >0 :
	print("x > 0 ")
else 
	print(" x= 0 ")

```
`elif`是else if的缩写.

# for 循环语句
python中的`for`语句与C语言的不同，它基于一个序列的子项来顺序迭代这个序列。这个序列可以是有范围的某种数据结构，例如数组、元组等，也可以是一串字符串。


```
def test_for():

    words = ['a','b','c','d']
    for word in words:
        print(word)

    str = "this is a string for test"
    for let in str :
        print(let)
```
那如果要实现从1到100的循环应该怎么做呢？Python提供了一个`range()`函数，它可以生成一个整数序列，作为参数传递给`list()`函数，可以产生一个整数元素的`list`，然后来进行循环：

```
    #计算0+1+2+...+100
    sum = 0
    for inter in list(range(100)):
        sum += inter
    print(sum)
```

# while 循环语句
`while`语句来判断循环条件是否成立，如果成立，则执行循环体，执行完成后再次判断条件是否成立，如此循环：
```
    i = 0
    sum = 0
    while i<100 :
        sum += i 
        i+=1
    print(sum)

```
每次循环，`i`的值都会增加1，当i=100时`i<100`条件不满足，便退出了循环。

# break 与 continue
与c语言类似，`break`用于结束`for`或者`while`的循环，而`continue`则跳出当前循环，继续进入下一轮循环中.

```
    i = 0 
    while i < 10:
        if i == 5: 
            break
        print(i,end=" ")

# output : 0 1 2 3 4 
```

```
    i = 0
    while i <10:
        if i == 5:
            continue
        print(i)
        i+=1
# output : 0 1 2 3 4 6 7 8 9
```
# 循环中的else子句

与C语言不同的是，Python提供与循环搭配的`else子句`,它在如下的情况会被执行：
- 对于for：迭代完整个循环列表时
- 对于while：执行条件为false时
- 如果循环是由于break退出时，则不会执行

例如：
```

    for i in list(range(10)):
        for j in list(range(5)):
            if i == 3: 
                break
            
        else:
	    print("in this loop ,i is ",i)

# output:
in this loop ,i is  0
in this loop ,i is  1
in this loop ,i is  2
in this loop ,i is  4
in this loop ,i is  5
in this loop ,i is  6
in this loop ,i is  7
in this loop ,i is  8
in this loop ,i is  9
```

这段代码中有两个嵌套的for循环，注意else子句是与第二个for循环对应的，而不是if语句。

# pass 语句
`pass` 语句的什么也不做，它作为一个占位符而存在，不影响代码执行的流程。它适合放置在那些语法上需要有语句，但是该语句什么也不用做的场合。例如：

```
while True:
	pass 

```
这是一个可以执行的死循环结构，按下`Ctrl+C`来结束循环。又例如在想自定义一个异常类，不过这个新的异常类不需要新的成员：

```
 class ServerException(Exception):
    pass

```
这里`ServerException`类继承自类`Exception`,它不需要自己实现新的成员。关于继承后面再介绍。

有时候我们在写代码时，喜欢先把接口的名称写出来，搭好整个程序代码流程的框架后再来详细设计接口实现，那么这时也可以使用`pass`来代替函数的实现：
```
def init():
    pass

def draw():
    pass 

def flush():
    pass 

def exit():
    pass

def act():
    pass()
    draw()
    flush()
    exit()
```






















